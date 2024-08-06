import requests
import json

def embed_text(input_data, ollama_url):
    try:
        payload = {"input": input_data, "model": "dolphin-llama3:8b"}
        print(f"Sending payload to Ollama: {payload}")  # Log the payload being sent

        response = requests.post(
            f"{ollama_url}/api/embed",  # Updated endpoint
            json=payload,
            stream=True
        )
        response.raise_for_status()
        
        # Collect response content
        response_data = ""
        for chunk in response.iter_content(chunk_size=8192):
            response_data += chunk.decode('utf-8')

        # Convert response data to JSON
        response_json = json.loads(response_data)
        print("Response JSON:", response_json)  # Log the response JSON for debugging
        
        # Check if 'embeddings' key exists and is not empty
        embeddings = response_json.get("embeddings")
        if not embeddings or not embeddings[0]:
            print("Error: Embeddings are empty or not found for input:", input_data)
            raise ValueError("Embeddings are empty or not found")

        return embeddings[0]
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        raise
    except (KeyError, IndexError, ValueError) as e:
        print("Error processing embeddings:", e)
        raise
