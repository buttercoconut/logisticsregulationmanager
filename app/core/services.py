# app/core/services.py
from sqlalchemy.orm import Session
from . import models
from .database import Base, engine
from datetime import datetime

# Create tables
Base.metadata.create_all(bind=engine)

# Service functions

def create_regulation(db: Session, regulation: models.RegulationCreate):
    # Auto-link law logic placeholder
    new_reg = models.Regulation(
        regulation_name=regulation.regulation_name,
        law_id=regulation.law_id,
        description=regulation.description,
        effective_date=regulation.effective_date,
        expiry_date=regulation.expiry_date,
        document_url=regulation.document_url,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(new_reg)
    db.commit()
    db.refresh(new_reg)
    # Record change history placeholder
    return new_reg

# Additional CRUD functions would be implemented similarly
