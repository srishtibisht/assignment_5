from sqlalchemy import select
from fastapi import HTTPException,status
from ..models import Appointment


def book_appointment(data, db):
    result = db.execute(
        select(Appointment).where(
            Appointment.doctor_id == data.doctor_id,
            Appointment.start_time < data.end_time,
            Appointment.end_time > data.start_time
        )
    )
    if not result.scalars().first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Slot already booked")

    appointment = Appointment(**data.dict(), patient_id=1)
    db.add(appointment)
    db.commit()
    db.refresh()
    return appointment
