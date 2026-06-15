from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class RegulationBase(BaseModel):
    regulation_name: str = Field(..., example="Road Transport Safety Regulation")
    law_id: int = Field(..., example=1)
    description: Optional[str] = Field(None, example="Regulation for safe road transport")
    effective_date: datetime = Field(..., example="2024-01-01T00:00:00Z")
    expiry_date: Optional[datetime] = Field(None, example="2030-12-31T23:59:59Z")
    document_url: Optional[str] = Field(None, example="https://example.com/doc.pdf")

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
