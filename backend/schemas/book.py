from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    author: str
    content: str