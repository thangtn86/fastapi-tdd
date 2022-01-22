from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.get('/status')
async def status(settings: Settings = Depends(get_settings)):
    return {
        'status': 'OK - Healthy',
        'env': settings.environment,
        'testing': settings.testing,
    }

