from ..repository import user_repo
from ..schemas import RegisterRequest,LoginRequest
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/auth",
    tags=["users"]
)


@router.post("/register",status_code=status.HTTP_201_CREATED)
def register_user(request:RegisterRequest,db:Session=Depends(get_db)):
    return user_repo.register_user(request,db)


@router.post("/login")
def login(request: LoginRequest,db:Session=Depends(get_db)):
    return user_repo.login_user(request,db)


@router.post("/forgot-password",status_code=status.HTTP_200_OK)
def forgot_password():
    return {"message": "Password reset link has been sent to your email"}






