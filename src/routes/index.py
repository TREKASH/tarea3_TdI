from fastapi import APIRouter  
  
from .hello import router as hello_router  
from .Chatbot import router as chatbot_router
router = APIRouter()  
  
router.include_router(hello_router, prefix="/hello")
router.include_router(chatbot_router, prefix="/chatbot")