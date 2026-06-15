from fastapi import FastAPI
from .app.api import regulations
app = FastAPI()
app.include_router(regulations.router)
