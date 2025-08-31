from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class AssignmentModel(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    course_id: str
    due_date: str
    created_at: str