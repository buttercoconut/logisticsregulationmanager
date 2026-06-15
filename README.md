# README.md
# Logistics Regulation Manager

This project provides a backend API for managing logistics regulations, linking them to laws, and maintaining an audit trail of changes.

## Features
- CRUD operations for regulations
- Link regulations to laws
- Audit history for every change
- FastAPI + SQLAlchemy stack
- Dockerized for easy deployment

## Getting Started

```bash
# Build the Docker image
docker build -t logistics-regulation-manager .

# Run the container
docker run -p 8000:8000 logistics-regulation-manager
```

The API will be available at `http://localhost:8000`.

## API Endpoints
- `POST /regulations/` – Create a new regulation
- (Additional endpoints for GET, PUT, DELETE will be added)

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```
