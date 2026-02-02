# from ast import pattern
from pydantic import BaseModel, Field, field_validator

class UserCreate(BaseModel):
    age: int    
    email: str | None = None
    # email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    email: str | None = Field(default=None, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # age 필드를 검증, 입력 값이 15 이상 40 미만인지 확인, age 변수에 저장 전에 실행
    @field_validator("age", mode="before")
    @classmethod
    def validate_age(cls, v: int) -> int:
        if v < 15 or v >= 40:
            raise ValueError("age must be >= 15 and < 40")
        return v
    
class UserOut(BaseModel):
    age: int 
    email: str | None = None