from pydantic import BaseModel

class Room(BaseModel):
    _id: str
    subject:str
    is_public:bool
    participants_count:int
    password:str
    participants_list:list
