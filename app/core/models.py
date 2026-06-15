# Document model placeholder
class DocumentBase(BaseModel):
    regulation_id: int
    file_name: str
    file_type: str
    file_url: str

class Document(DocumentBase):
    document_id: int

    class Config:
        orm_mode = True

# User model placeholder
class UserBase(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_active: bool = True

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
