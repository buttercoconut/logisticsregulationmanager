# services.py
from sqlalchemy.orm import Session
from . import models
from .database import Base, engine
from datetime import datetime

# Create tables
Base.metadata.create_all(bind=engine)

# Regulation CRUD

def create_regulation(db: Session, regulation: models.RegulationCreate):
    db_reg = models.Regulation(**regulation.dict())
    db.add(db_reg)
    db.commit()
    db.refresh(db_reg)
    # Add history
    history = models.RegulationHistory(
        regulation_id=db_reg.regulation_id,
        changed_by=1,  # placeholder
        change_type="CREATE",
        change_data=str(regulation.dict()),
    )
    db.add(history)
    db.commit()
    return db_reg

# Additional CRUD functions would follow similar pattern
