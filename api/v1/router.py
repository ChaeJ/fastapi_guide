from fastapi import APIRouter
from .users import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(users_router, prefix="/resp", tags=["responses"])
