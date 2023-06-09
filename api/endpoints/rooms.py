from fastapi import APIRouter, HTTPException, Header
from models.Response import Response
from models.User import User
from repositories.RoomRepo import RoomRepo
from repositories.UserRepo import UserRepo
from schemas import room
router = APIRouter()

@router.post("/room/")
async def create_room( room_setting: room.roomCreate, Authorization: str | None = Header(default=None)):
    try:
        print('catch POST /room ')
        access_token = Authorization.replace("Bearer ", "")
        user_info = await UserRepo.findUserByAccessToken(access_token)
        room_info = await RoomRepo.insert(user_info, room_setting)
        print(room_info)
        return Response(code=200, status="OK", message="Success", data={'room_info' : room_info}).dict(exclude_none=True)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,  detail='새로운 방 생성에 실패하였습니다.')
    
@router.get("/room/")
async def read_room():
    try:
        print('catch GET /room ')
        room_list = await RoomRepo.retrieve()
        return Response(code=200, status="OK", message="Success", data=room_list).dict(exclude_none=True)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,  detail='방 조회에 실패하였습니다.')
    
@router.post("/room/join")
async def join_room(payload: dict, Authorization: str | None = Header(default=None)):
    try:
        print('catch POST /room/join')
        room_id = payload['room_id']
        print(room_id)
        access_token = Authorization.replace("Bearer ", "")
        user_info = await UserRepo.findUserByAccessToken(access_token)
        status, updated_room = await RoomRepo.joinRoomById(room_id, user_info)
        if status :
            return Response(code=200, status="OK", message="Success", data=updated_room).dict(exclude_none=True)
        else :
            raise HTTPException(status_code=400,  detail='방 입장에 실패하였습니다.') 
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,  detail='방 입장에 실패하였습니다.')
