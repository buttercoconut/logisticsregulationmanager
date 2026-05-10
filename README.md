# Logistics Regulation Manager Backend

This repository contains the backend implementation for the Logistics Regulation Manager application. It is built with FastAPI, SQLAlchemy, and PostgreSQL.

## Project Structure

```
/logisticsregulationmanager
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── law.py
│   │   ├── regulation.py
│   │   └── user.py
│   └── core
│       ├── __init__.py
│       ├── database.py
│       ├── models.py
│       └── services.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup

```bash
# Build the Docker image
docker build -t logistics-regulation-manager .

# Run the container
docker run -d -p 8000:8000 --name lr-manager logistics-regulation-manager
```

## API Endpoints

- **/laws/** – CRUD operations for laws.
- **/regulations/** – CRUD operations for regulations.
- **/users/** – User registration.

## License

MIT License
