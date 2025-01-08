from dataclasses import dataclass

@dataclass
class Task:
    title: str
    description: str
    task_status: bool
    user_id: str
    task_id:str