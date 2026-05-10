from fastapi import FastAPI
from .api import law, regulation, user

app = FastAPI(title="Logistics Regulation Manager API")

app.include_router(law.router)
app.include_router(regulation.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Logistics Regulation Manager API"}
