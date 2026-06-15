# api/regulation.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core import models, services
from ..core.database import get_db

router = APIRouter(prefix="/regulations", tags=["regulations"])

@router.post("/", response_model=models.Regulation)
async def create_regulation(regulation: models.RegulationCreate, db: Session = Depends(get_db)):
    try:
        return services.create_regulation(db, regulation)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Additional endpoints (GET, PUT, DELETE) would be added here
