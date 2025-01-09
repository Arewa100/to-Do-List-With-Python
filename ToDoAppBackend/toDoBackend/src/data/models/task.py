from bson import ObjectId
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    task_status: bool
    user_id: str
    task_id:str = None