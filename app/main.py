from fastapi import FastAPI
from app.routes.chat_route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Multi-Agent Coding Assistant Running"
    }