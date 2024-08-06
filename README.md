# Chat with Files 🤖 📖 📄

A Proof of Concept (POC) Retrieval-Augmented Generation (RAG) application that allows chatting with PDFs, CSVs, and XLS files. This application leverages FastAPI for the backend, Streamlit for the frontend, ChromaDB for vector storage, and Ollama3 for generating text embeddings.

## Features

- Upload and process PDF, CSV, and XLS files
- Generate embeddings for documents using Ollama3
- Store and retrieve document embeddings using ChromaDB
- Query documents and get relevant responses
- User-friendly interface using Streamlit

## Prerequisites

- Docker
- Docker Compose
- Poetry (for dependency management)
- Ollama3 (installed and running locally)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/rag-app.git
   cd rag-app
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Ensure Ollama3 is installed and running on your local machine:

   ```bash
   # Install Ollama3 if not already installed
   # Refer to Ollama3 documentation for installation steps

   # Start Ollama3
   ollama start
   ```

## Running the Application

### Using Docker Compose

1. Navigate to the `docker` directory:

   ```bash
   cd docker
   ```

2. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

3. Access the frontend:

   Open your browser and go to `http://localhost:8501` to interact with the Streamlit application.

### Backend

The backend is built with FastAPI and includes the following modules:

- `main.py`: FastAPI application and API endpoints
- `utils.py`: Utility functions for indexing and querying documents
- `document_processing.py`: Functions for extracting text from PDF, CSV, and XLS files
- `embedding.py`: Functions for generating embeddings using Ollama3
- `indexing.py`: Functions for creating and querying the ChromaDB index

### Frontend

The frontend is built with Streamlit and includes the following module:

- `app.py`: Streamlit application code

### Docker

The Docker setup includes:

- `Dockerfile`: Dockerfile for the services
- `docker-compose.yml`: Docker Compose configuration file

## Usage

1. **Upload Files**: Use the Streamlit interface to upload PDF, CSV, or XLS files.
2. **Query Documents**: Enter your query in the text input field and get relevant responses from the uploaded documents.

## Environment Variables

The application uses the following environment variables:

- `CHROMA_URL`: URL for the ChromaDB service (default: `http://localhost:8000`)
- `OLLAMA_URL`: URL for the Ollama3 service (default: `http://localhost:5000`)

These variables are set in the `docker-compose.yml` file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://www.streamlit.io/)
- [ChromaDB](https://github.com/chromadb/chromadb)
- [Ollama3](https://ollama.com/)

## Troubleshooting

### Common Issues

1. **Container fails to start**:

   - Check if the required ports (8000, 8001, 8501) are available and not being used by other applications.
   - Ensure Docker and Docker Compose are properly installed and running.

2. **Issues with dependencies**:

   - Make sure you have the latest version of Poetry installed.
   - Verify that all dependencies in the `pyproject.toml` file are correctly specified.

3. **Database connection issues**:
   - Ensure the ChromaDB service is running and accessible at the specified URL.
   - Verify that the `CHROMA_URL` environment variable is correctly set.

### Support

If you encounter any issues or have questions, feel free to open an issue on GitHub or contact the maintainers.

## Future Work

- Add support for more document types (e.g., DOCX)
- Enhance the query interface with more advanced search options
- Implement authentication and authorization for secure access
- Optimize embedding and search performance
