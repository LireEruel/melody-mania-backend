import pprint

from pymongo import ReturnDocument
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
    
    @staticmethod
    async def findRoomById(target_room_id):
        query= {
            '_id' : target_room_id
        }
        targetRoom = None
        async for crt_room in database.get_collection('room').find(query):
            targetRoom = crt_room
            break

        return targetRoom

    @staticmethod
    async def joinRoomById(target_room_id, join_user):
        try :
            query = {
            '_id': target_room_id
            }
            update = {
                "$push": {
                    "participants_list": join_user 
                }
            }
            return_document = ReturnDocument.AFTER
            updated_room = await database.get_collection("room").find_one_and_update(query, update, return_document = ReturnDocument.AFTER)
            for key, value in updated_room.items():
                print(f"{key}: {value}")
            return True, updated_room
        except Exception as e:
            print(e)
            return {'status': False}

