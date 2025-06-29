from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskData(BaseModel):
    model_config = ConfigDict(from_attributes=True) #молитва для устранения ошибок со схемами
    id: Optional[int] = None
    author: str
    content: str


class ReadTask(BaseModel):
    email: str

