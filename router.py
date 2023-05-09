from fastapi import APIRouter, HTTPException
from repository import UserRepo
from model import User, Response

router = APIRouter()

@router.post("/user/")
async def signup(user: User):
    check_unique_res = await UserRepo.checkUniqueUser(user)
    if  check_unique_res['is_unique'] :
        print(check_unique_res['is_unique'])
        await UserRepo.insert(user)
        return Response(code=200, status="OK", message="Success").dict(exclude_none=True)
    else :
        same_user = check_unique_res['existing_user']
        if user.name == same_user['name'] :
            raise HTTPException(status_code=400,  detail="이미 같은 이름의 유저가 있습니다.")
        elif user.email == same_user['email'] :
            raise HTTPException(status_code=400,  detail="이미 등록된 이메일 입니다.")
        else :
             return Response(code=200, status="OK", message="Success").dict(exclude_none=True)

@router.get("/user/")
async def retrieve():
    _userList = await UserRepo.retrieve()
    return Response(code=200, status="OK", message="Success", data = _userList).dict(exclude_none=True) 