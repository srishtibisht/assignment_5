from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "SUPER_SECRET"
ALGORITHM = "HS256"
EXPIRE_TIME = 60

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def  verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict, expires_minutes: int = EXPIRE_TIME):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=expires_minutes)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


