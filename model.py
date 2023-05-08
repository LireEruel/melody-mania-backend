from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class User(BaseModel):
    id: str = None
    name: str
    email: str
    password: str


class Response(BaseModel):
    code: str
    status: str
    message: str
    data: Optional[T] = None