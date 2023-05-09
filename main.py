from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router

app = FastAPI()
# CORS middleware 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=['*'],  # 모든 HTTP 메소드 허용
    allow_headers=['*'],  # 모든 헤더 허용
)

@app.get('/')
async def Home():
    return "welcome home"

app.include_router(api_router)