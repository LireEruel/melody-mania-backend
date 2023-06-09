from pydantic import BaseModel

class Music(BaseModel):
    _id: str = None
    music_name: str
    singer: str
    play_url: str
    tags: list
