from pydantic import BaseModel
from datetime import datetime, timezone


class Task(BaseModel):
    title: str = None
    description: str = None
    task_status: bool = None
    user_id: str= None
    task_id:str = None
    date_created: datetime = datetime.now(timezone.utc)