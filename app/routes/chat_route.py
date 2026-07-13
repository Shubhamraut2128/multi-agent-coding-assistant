from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.graph.workflow import run_workflow

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    response = run_workflow(
        request.question
    )

    return {
        "response": response
    }