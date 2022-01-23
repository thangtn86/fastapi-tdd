from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/status")
async def status(settings: Settings = Depends(get_settings)):
    return {
        "status": "OK - Healthy",
        "env": settings.environment,
        "testing": settings.testing,
    }
