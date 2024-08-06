from chromadb import Client

def create_index(embeddings, documents):
    client = Client()
    collection = client.create_collection("my_collection")

    # Use upsert with the correct parameters
    ids = [str(i) for i in range(len(documents))]
    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        metadatas=[{"document": document} for document in documents]
    )
    
    return collection

def search_index(collection, query_embedding):
    results = collection.query(query_embedding)
    return results
