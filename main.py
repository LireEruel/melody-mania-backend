import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router
from fastapi.responses import HTMLResponse

from socket_handler.recv_handler import recv_handler
app = FastAPI()
# CORS middleware 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=['*'],  # 모든 HTTP 메소드 허용
    allow_headers=['*'],  # 모든 헤더 허용
)

class User:
    def __init__(self, user_id: str, websocket: WebSocket):
        self.user_id = user_id
        self.websocket = websocket

connected_users: list[User] = []


@app.get('/')
async def Home():
    return "welcome home"

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()

    user = User(user_id, websocket)
    connected_users.append(user)

    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            recv_handler(data)
            # 원하는 작업 수행

    except Exception as e:
        print(f"WebSocket error: {e}")
    
    finally:
        connected_users.remove(user)

# 특정 사용자에게 소켓 보내기
async def send_socket_to_user(user_id: str, data: str):
    user = next((u for u in connected_users if u.user_id == user_id), None)
    if user:
        await user.websocket.send_text(data)
    else:
        print(f"User with ID {user_id} not found.")