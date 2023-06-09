from fastapi import APIRouter, HTTPException, Header
from models.Response import Response
from models.User import User
from repositories.MusicRepo import MusicRepo
from repositories.UserRepo import UserRepo
from models.Music import Music
router = APIRouter()

@router.post("/music/")
async def create_room( music_info: Music, Authorization: str | None = Header(default=None)):
    try:
        print('catch POST /music ')
        print(music_info, Authorization)
        access_token = Authorization.replace("Bearer ", "")
        user_info = await UserRepo.findUserByAccessToken(access_token)
        if user_info is None :
             raise HTTPException(status_code=400,  detail='로그인 후 사용해주세요.')
        music_info = await MusicRepo.insert(music_info)
        print(music_info)
        return Response(code=200, status="OK", message="Success", data={'music_info' : music_info}).dict(exclude_none=True)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,  detail='새로운 음악 등록에 실패하였습니다.')
    
@router.get("/room/")
async def read_room():
    try:
        print('catch GET /room ')
        music_list = await MusicRepo.retrieve()
        return Response(code=200, status="OK", message="Success", data=music_list).dict(exclude_none=True)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,  detail='음악 목록 조회에 실패하였습니다.')