from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core import services, models
from ..core.services import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=models.User)
async def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)
