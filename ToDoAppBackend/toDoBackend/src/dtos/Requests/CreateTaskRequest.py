from pydantic import BaseModel

class CreateTaskRequest(BaseModel):
        title:str = None
        description:str = None
        task_status:bool = None
        user_id:str = None

