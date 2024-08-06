from .document_processing import process_file
from .embedding import embed_text
from .indexing import create_index, search_index

def index_file(file_path, ollama_url):
    text = process_file(file_path)
    documents = text.split("\n")  # Assuming each line is a separate document
    valid_embeddings = []
    valid_documents = []
    for doc in documents:
        try:
            embedding = embed_text(doc, ollama_url)
            valid_embeddings.append(embedding)
            valid_documents.append(doc)
        except ValueError as e:
            print(f"Skipping document due to error: {e}")

    if not valid_embeddings:
        raise ValueError("No valid embeddings found for any documents.")
    
    collection = create_index(valid_embeddings, valid_documents)
    return collection

def handle_query(query, collection, ollama_url):
    query_embedding = embed_text(query, ollama_url)
    results = search_index(collection, query_embedding)
    return results
