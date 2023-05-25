from typing import Optional

from pydantic import BaseModel


# Shared properties
class roomCreate(BaseModel):
    subject:str
    is_public:bool
    participants_count:int
    password:str = None