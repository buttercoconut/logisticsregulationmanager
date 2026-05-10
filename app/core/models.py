# app/core/models.py
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class RegulationBase(BaseModel):
    regulation_name: str
    law_id: int
    description: Optional[str] = None
    effective_date: datetime
    expiry_date: Optional[datetime] = None
    document_url: Optional[str] = None

class RegulationCreate(RegulationBase):
    pass

class RegulationUpdate(RegulationBase):
    pass

class Regulation(RegulationBase):
    regulation_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
