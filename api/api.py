from fastapi import APIRouter

from api.endpoints import login, users, rooms

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(login.router)
api_router.include_router(rooms.router)