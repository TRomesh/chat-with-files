import streamlit as st
import requests

# Constants
BACKEND_URL = "http://localhost:8001"

# Function to upload file
def upload_file(file):
    files = {"file": file}
    response = requests.post(f"{BACKEND_URL}/upload", files=files)
    return response.json()

# Function to query the document
def query_document(query):
    params = {"query": query}
    response = requests.get(f"{BACKEND_URL}/query", params=params)
    return response.json()

# Streamlit UI
st.title("Chat with Your Files")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "csv", "xls", "xlsx"])

if uploaded_file is not None:
    st.write("Uploading and processing file...")
    upload_response = upload_file(uploaded_file)
    st.write(upload_response)

# Query input
query = st.text_input("Enter your query:")

if query:
    st.write("Querying the document...")
    query_response = query_document(query)
    st.write(query_response)

    # Extracting and displaying the generated answer
    if "response" in query_response:
        answer = query_response["response"]
        st.write("Generated Answer:")
        st.write(answer)