from fastapi import APIRouter

from app.models.schemas import ChatRequest
from app.agents.agent import SalesAgent
from app.memory.sqlite_memory import SQLiteMemory

router = APIRouter()

agent = SalesAgent()

memory = SQLiteMemory()


@router.post("/chat/{user_id}")
def chat(user_id: str, request: ChatRequest):

    response = agent.chat(
        user_id=user_id,
        message=request.message
    )

    return response


@router.get("/chat/{user_id}/history")
def get_history(user_id: str):

    history = memory.get_history(user_id)

    formatted_history = []

    for msg in history:

        formatted_history.append({
            "role": msg.role,
            "content": msg.content,
            "session_id": msg.session_id
        })

    return {
        "user_id": user_id,
        "history": formatted_history
    }


@router.delete("/chat/{user_id}/memory")
def clear_memory(user_id: str):

    memory.clear_memory(user_id)

    return {
        "message": f"Memory cleared for {user_id}"
    }