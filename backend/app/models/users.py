from pydantic import BaseModel, EmailStr
from bson import ObjectId
from typing import Optional

class User(BaseModel):
   id: Optional[str]
   name: str
   email: EmailStr
   password_hash: str
   role: str # so this gotta be teacher or student or admin
   