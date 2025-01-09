from datetime import datetime, timezone
from pydantic import BaseModel
from pydantic.v1 import NoneStr


class CreateTaskResponse(BaseModel):
    title: str = None
    description: str = None
    task_status: str = None
    user_id: str = None
    task_id: str = None
    date_created: str = None