from pydantic import BaseModel

class User(BaseModel):
    username: str = None
    email: str = None
    password:str = None
    id: str = None