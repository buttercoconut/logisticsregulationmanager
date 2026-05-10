# app/main.py
from fastapi import FastAPI
from .api import regulation, law, user

app = FastAPI(title="Logistics Regulation Manager")

app.include_router(regulation.router)
app.include_router(law.router)
app.include_router(user.router)

# Additional startup/shutdown events can be added here
