from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Response(BaseModel):
    code: str
    status: str
    message: str
    data: Optional[T] = None