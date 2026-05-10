from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core import services, models
from ..core.services import get_db

router = APIRouter(prefix="/regulations", tags=["regulations"])

@router.post("/", response_model=models.Regulation)
async def create_regulation(regulation: models.RegulationCreate, db: Session = Depends(get_db)):
    return services.create_regulation(db, regulation)

@router.get("/", response_model=list[models.Regulation])
async def read_regulations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Regulation).offset(skip).limit(limit).all()

@router.get("/{regulation_id}", response_model=models.Regulation)
async def read_regulation(regulation_id: int, db: Session = Depends(get_db)):
    reg = services.get_regulation(db, regulation_id)
    if reg is None:
        raise HTTPException(status_code=404, detail="Regulation not found")
    return reg
