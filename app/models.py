from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime


class User(BaseModel):
    username:str
    password_hash:str


class Task(BaseModel):
    task_id:str
    owner:str
    content:str
    tags:List[str] = []
    complated:bool = False
    created_time: datetime = datetime.now().isoformat()

