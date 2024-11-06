from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def get_bands():
    return {"Say": "Hello!"} 