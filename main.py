from fastapi import FastAPI
from .router import user, doctor, appointments
from . import schemas,models
from .database import engine,get_db


models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(doctor.router)
app.include_router(appointments.router)


