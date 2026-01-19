from ..import models
from ..schemas import RegisterRequest,LoginRequest
from sqlalchemy.orm import Session as Session
from ..router.authentication import pwd_context,verify_password
from router.authentication import pwd_context,verify_password,create_access_token

def register_user(request: RegisterRequest, db:Session):
    request.password = pwd_context.hash(request.password)  # Placeholder for password handling
    new_user = models.User(request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def register_user(request:UserLogin,db:Session):
    user = db.query(models.User).filter(models.User.email==request.username).first()

    verfifcation = verify_password(request.password,user.password)
    
    if not verfifcation:
        return "Invalid Credentials or User not exists"
    else:
        return create_access_token(user.dict())
 