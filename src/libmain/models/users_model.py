from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    job: Optional[str] = None
    status: Optional[str] = False

    class Config:
        orm_mode = True
