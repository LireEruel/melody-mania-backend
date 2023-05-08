from fastapi import APIRouter
from repository import UserRepo
from model import User, Response

router = APIRouter()

@router.post("/user/")
async def signup(user: User):
    _userList = await UserRepo.insert(user)
    return Response(code=200, status="OK", message="Success").dict(exclude_none=True)

@router.get("/user/")
async def retrieve():
    _userList = await UserRepo.retrieve()
    return Response(code=200, status="OK", message="Success", data = _userList).dict(exclude_none=True) 