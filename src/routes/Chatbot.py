from fastapi import APIRouter
from pydantic import BaseModel
from src.services.query_index import query_index


router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("")
async def chat(request: ChatRequest):
    response_text = query_index(request.query)

    return {"answer": response_text}
