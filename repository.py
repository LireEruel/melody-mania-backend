from model import *
from config import database
import uuid

class UserRepo():

    @staticmethod
    async def retrieve():
        _user = []
        collection = database.get_collection('user').find()
        async for user in collection:
            _user.append(user)
        return _user


    @staticmethod
    async def insert(user: User):
        id = str(uuid.uuid4())
        _user = {
            "_id" : id,
            "name" : user.name,
            "email" : user.email,
            "password" : user.password
        }
        await database.get_collection('user').insert_one(_user)