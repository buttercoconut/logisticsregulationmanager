# app/api/regulation.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core import models, services
from ..core.database import get_db

router = APIRouter(prefix="/regulations", tags=["regulations"])

@router.post("/", response_model=models.Regulation)
def create_regulation(reg: models.RegulationCreate, db: Session = Depends(get_db)):
    try:
        return services.create_regulation(db, reg)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Placeholder for list and detail endpoints
