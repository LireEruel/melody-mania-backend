from config import database
import uuid
from schemas.room import roomCreate
from models.User import User
class RoomRepo():

    @staticmethod
    async def retrieve():
        _rooms = []
        collection = database.get_collection('room').find()
        async for room in collection:
            _rooms.append(room)
        return _rooms
    
    @staticmethod
    async def insert(user : User ,room_info: roomCreate):
        id = str(uuid.uuid4())
        _room = {
            "_id" : id,
            "subject" : room_info.subject,
            "is_public" : room_info.is_public,
            "participants_count" : room_info.participants_count,
            "password" : room_info.password,
            'participants_list' : [user]
        }
        await database.get_collection('room').insert_one(_room)
        return _room