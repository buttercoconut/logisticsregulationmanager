from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core import services, models
from ..core.services import get_db

router = APIRouter(prefix="/laws", tags=["laws"])

@router.post("/", response_model=models.Law)
async def create_law(law: models.LawCreate, db: Session = Depends(get_db)):
    db_law = services.get_law(db, law_id=law.law_id) if hasattr(law, "law_id") else None
    if db_law:
        raise HTTPException(status_code=400, detail="Law already exists")
    return services.create_law(db, law)

@router.get("/", response_model=list[models.Law])
async def read_laws(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_laws(db, skip=skip, limit=limit)

@router.get("/{law_id}", response_model=models.Law)
async def read_law(law_id: int, db: Session = Depends(get_db)):
    db_law = services.get_law(db, law_id)
    if db_law is None:
        raise HTTPException(status_code=404, detail="Law not found")
    return db_law
