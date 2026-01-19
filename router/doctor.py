from ..repository import doctor_repo
from ..schemas import doctor_schema
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User


router = APIRouter(
    prefix="/doctors",
    tags=["doctors"]
)

@router.get("")
def list_doctors(db: Session = Depends(get_db)):
    return doctor_repo.doctors(db)




