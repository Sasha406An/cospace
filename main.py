from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CoSpace - Система бронирования рабочих мест", version="1.0.0")

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/resources/", response_model=schemas.ResourceResponse)
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    db_res = db.query(models.Resource).filter(models.Resource.name == resource.name).first()
    if db_res:
        raise HTTPException(status_code=400, detail="Resource name already exists")
    new_resource = models.Resource(name=resource.name, type=resource.type, price=resource.price)
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

@app.get("/resources/", response_model=list[schemas.ResourceResponse])
def get_resources(db: Session = Depends(get_db)):
    return db.query(models.Resource).all()

@app.post("/bookings/", response_model=schemas.BookingResponse)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == booking.user_id).first()
    res = db.query(models.Resource).filter(models.Resource.id == booking.resource_id).first()
    if not user or not res:
        raise HTTPException(status_code=404, detail="User or Resource not found")

    if booking.start_time >= booking.end_time:
        raise HTTPException(status_code=400, detail="Start time must be before end time")

    overlapping_booking = db.query(models.Booking).filter(
        models.Booking.resource_id == booking.resource_id,
        models.Booking.start_time < booking.end_time,
        models.Booking.end_time > booking.start_time
    ).first()

    if overlapping_booking:
        raise HTTPException(status_code=400, detail="This resource is already booked for the selected time slot.")

    new_booking = models.Booking(
        user_id=booking.user_id,
        resource_id=booking.resource_id,
        start_time=booking.start_time,
        end_time=booking.end_time
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking