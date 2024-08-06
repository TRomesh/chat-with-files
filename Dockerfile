# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install build-essential and other necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the poetry lock file and pyproject.toml from the root directory of the project
COPY pyproject.toml poetry.lock* ./

# Install poetry
RUN pip install poetry

# Install hnswlib separately to avoid PEP 517 issues
RUN pip install hnswlib==0.8.0

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy the entire project source code into the container
COPY . .

# Expose the ports the apps run on
EXPOSE 8001 8501

# Start both the backend and frontend
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8001 & streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0"]
