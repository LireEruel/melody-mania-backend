from fastapi import APIRouter, HTTPException
from models.Response import Response
from models.User import User
from repositories.UserRepo import UserRepo
from schemas import user
from util.jwtToken import generate_jwt

router = APIRouter()

@router.post("/login/")
async def login(login_data:user.UserLogin):
    email = login_data.email
    password = login_data.password
    print('/login/')
    user = await UserRepo.findUserByEmail(email)
    print('find user')
    print(user)
    if isinstance(user, type(None)):
        raise HTTPException(status_code=402, detail='가입된 메일이 아닙니다.') 
    else:
        if(user['password'] == password):
            access_token = generate_jwt(user['_id'])
            await UserRepo.setAccessToken(user['_id'], access_token)
            del user['password']
            return Response(code=200, status="OK", message="Success",data={'user_info' : user}).dict(exclude_none=True)
        else :
            raise HTTPException(status_code=401, detail='비밀번호가 일치하지 않습니다.')