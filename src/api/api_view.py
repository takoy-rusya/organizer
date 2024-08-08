from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["HEALTH"])
async def get_health_check():
    return {'status': 'ok'}
