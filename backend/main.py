from fastapi import FastAPI, UploadFile, File
from .utils import index_file, handle_query
import os
import aiofiles

app = FastAPI()

collection = None  # Global variable to store the ChromaDB collection

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global collection
    
    # Save the uploaded file to disk
    file_path = f"/tmp/{file.filename}"
    async with aiofiles.open(file_path, 'wb') as out_file:
        while content := await file.read(1024):  # Read the file in chunks
            await out_file.write(content)
    
    # Process the file
    collection = index_file(file_path, OLLAMA_URL)
    return {"filename": file.filename}

@app.get("/query")
async def query_document(query: str):
    results = handle_query(query, collection, OLLAMA_URL)
    return {"response": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
