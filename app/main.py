# main.py
from fastapi import FastAPI
from .api import regulation

app = FastAPI(title="Logistics Regulation Manager API")

app.include_router(regulation.router)

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to Logistics Regulation Manager API"}
