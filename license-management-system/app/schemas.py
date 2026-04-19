from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class LicenseCreate(BaseModel):
    name: str
    expiry_date: date