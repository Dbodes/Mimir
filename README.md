# Mimir: A Local RAG System

Mimir is an open-source project that enables you to run a local Retrieval-Augmented Generation (RAG) system without relying on third-party APIs. It integrates a modern Flutter front-end, a Python backend using FastAPI, Milvus for efficient vector storage, and DeepSeek for local LLM inference—all orchestrated using Docker Compose—to offer a scalable and privacy-focused solution for document querying and processing.

## Table of Contents
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage Instructions](#usage-instructions)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Local RAG System:** Query documents using an intuitive chat-like interface that retrieves and combines relevant document snippets locally.
- **Modular Architecture:**
  - **Flutter Front-End:** Provides a responsive UI.
  - **Python Backend (FastAPI):** Manages query processing and document ingestion.
  - **Milvus:** Efficient vector storage and retrieval.
  - **DeepSeek:** Local LLM inference.
- **Containerized Deployment:** Simplified setup using Docker Compose.
- **Privacy-Focused:** All data is processed locally.

## Architecture Overview
Mimir consists of three main components:
- **mimir_app:** The Flutter application.
- **backend:** The Python FastAPI backend.
- **deepseek:** A service wrapping DeepSeek for LLM inference.
These parts are connected via Docker Compose, ensuring a consistent environment.

## Getting Started

### Prerequisites
Ensure the following are installed:
- Docker and Docker Compose
- Flutter SDK
- Python 3.9 or later

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Dbodes/Mimir.git
   cd Mimir
   ```
2. **Start the Containers:**
   ```bash
   docker-compose up --build
   ```
3. **Run the Flutter App:**
   Open a new terminal, navigate to the Flutter project folder, and run:
   ```bash
   cd mimir_app
   flutter pub get
   flutter run
   ```

## Usage Instructions
- **Document Ingestion:** Run the ingestion scripts in the backend (using LlamaIndex) to index your documents.
- **Querying:** Use the Flutter interface to submit queries. The backend retrieves relevant document segments, forwards context to DeepSeek, and returns an answer.
- **Advanced Commands:** Special commands (e.g., visualization triggers) can be used for additional functionality.

## Troubleshooting
- **Docker Issues:** Ensure Docker and Docker Compose are correctly installed.
- **Container Logs:** Check logs using:
  ```bash
  docker-compose logs
  ```
- **Network Issues:** Confirm containers can communicate on the designated ports.

## Contributing
Contributions are welcome:
- Open an issue to discuss ideas.
- Fork the repository, commit changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.