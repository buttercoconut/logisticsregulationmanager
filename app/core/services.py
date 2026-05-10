from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Law, Regulation, User
from .models import LawCreate, Law as LawModel, RegulationCreate, Regulation as RegulationModel, UserCreate, User as UserModel
from typing import List

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Law services

def create_law(db: Session, law: LawCreate):
    db_law = Law(law_name=law.law_name, description=law.description)
    db.add(db_law)
    db.commit()
    db.refresh(db_law)
    return db_law

def get_law(db: Session, law_id: int):
    return db.query(Law).filter(Law.law_id == law_id).first()

def get_laws(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Law).offset(skip).limit(limit).all()

# Regulation services

def create_regulation(db: Session, regulation: RegulationCreate):
    db_reg = Regulation(
        regulation_name=regulation.regulation_name,
        law_id=regulation.law_id,
        description=regulation.description,
        effective_date=regulation.effective_date,
        expiry_date=regulation.expiry_date,
        document_url=regulation.document_url,
    )
    db.add(db_reg)
    db.commit()
    db.refresh(db_reg)
    return db_reg

def get_regulation(db: Session, regulation_id: int):
    return db.query(Regulation).filter(Regulation.regulation_id == regulation_id).first()

# User services (simplified)

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = "fakehashed" + user.password
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=fake_hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Additional services can be added here
