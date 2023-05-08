from fastapi import FastAPI
import router

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home"

app.include_router(router.router)