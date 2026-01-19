from ..import models
from ..import schemas
from sqlalchemy.orm import Session as Session
from fastapi import APIRouter, Depends, HTTPException, status



def doctors(db:Session):
    user = db.query(models.User).filter(models.User.email=="doctor").all()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
   
    return user