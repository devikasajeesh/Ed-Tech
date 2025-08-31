from pydantic import BaseModel
from typing import Optional, List
from bson import ObjectId

class ClassModel(BaseModel):
   id: Optional[str]
   name: str
   description: str
   teacher_id: str
   student_ids: List[str] = []
