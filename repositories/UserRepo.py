from config import database
import uuid

from models.User import User

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

    @staticmethod
    async def checkUniqueUser(user: User):
        query = {
            '$or': [
                {'name': user.name},
                {'email': user.email}
            ]
        }
        res = {
            'is_unique' : True,
            'existing_user' : None
        }

        async for crt_user in database.get_collection('user').find(query):
            res['is_unique'] = False
            res['existing_user'] = crt_user
            break
        
        return res