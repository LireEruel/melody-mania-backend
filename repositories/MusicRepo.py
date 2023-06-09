from pymongo import ReturnDocument
from config import database
import uuid
from models.Music import Music
class MusicRepo():

    @staticmethod
    async def retrieve():
        _musics = []
        collection = database.get_collection('music').find()
        async for music in collection:
            _musics.append(music)
        return _musics
    
    @staticmethod
    async def insert(music_info: Music):
        id = str(uuid.uuid4())
        _music = {
            "_id" : id,
            "music_name" : music_info.music_name,
            "singer" : music_info.singer,
            "play_url" : music_info.play_url,
            "singer" : music_info.singer
        }
        await database.get_collection('music').insert_one(_music)
        return _music
    
    @staticmethod
    async def findMusicById(target_music_id):
        query= {
            '_id' : target_music_id
        }
        targetMusic = None
        async for crt_music in database.get_collection('msuic').find(query):
            targetMusic = crt_music
            break

        return targetMusic