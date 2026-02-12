from fastapi import APIRouter

from .resp import router as resp
from .users import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(resp, prefix="/resp", tags=["res", "responses"])
