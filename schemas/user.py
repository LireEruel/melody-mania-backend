from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserLogin(BaseModel):
    email: str
    password:str