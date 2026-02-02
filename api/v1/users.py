from fastapi import APIRouter, Depends
from depends.admin_only import admin_validator
from schemas.users import UserCreate, UserOut

router = APIRouter()

@router.get("/")
async def list_users(admin_only: bool = Depends(admin_validator)):
    if not admin_only:
        return []
    
    return ["user1", "user2", "user3"]

@router.post("/create", response_model=UserOut)
async def create_user(user:UserCreate):
    return user