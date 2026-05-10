from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class RegulationBase(BaseModel):
    regulation_name: str = Field(..., example="Road Transport Safety Regulation")
    law_id: int
    description: Optional[str] = None
    effective_date: datetime
    expiry_date: Optional[datetime] = None
    document_url: Optional[str] = None

class RegulationCreate(RegulationBase):
    pass

class RegulationUpdate(BaseModel):
    regulation_name: Optional[str] = None
    law_id: Optional[int] = None
    description: Optional[str] = None
    effective_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    document_url: Optional[str] = None

class Regulation(RegulationBase):
    regulation_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class LawBase(BaseModel):
    law_name: str
    description: Optional[str] = None

class LawCreate(LawBase):
    pass

class Law(LawBase):
    law_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
