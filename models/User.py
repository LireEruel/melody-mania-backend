from pydantic import BaseModel

class User(BaseModel):
    _id: str = None
    name: str
    email: str
    password: str
    is_superuser  = bool 
    access_token: str = None
