from pydantic import BaseModel, EmailStr
from datetime import datetime

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    role: str
    name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AppointmentCreate(BaseModel):
    doctor_id: int
    start_time: datetime
    end_time: datetime
