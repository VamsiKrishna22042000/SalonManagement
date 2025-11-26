from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session,selectinload,load_only

from ..config.db_connection import get_session
from ..schemas.booking_schema import BookingP
from ..models.booking_model import Booking
from ..models.staff_service_model import Service,Staff,Salon
from ..models.user_model import User

from ..config.auth import validate_token

booking_router = APIRouter(prefix="",tags=["Bookings"],dependencies=[Depends(validate_token)])

@booking_router.post("/booking")
def book_slot(bookingobject:BookingP,db:Session=Depends(get_session)):
    
    check_salon = db.query(Salon).filter(Salon.id == bookingobject.salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon Does not exists!")
    
    check_staff = db.query(Staff).filter(Staff.id == bookingobject.staff_id).first()

    if not check_staff:

        raise HTTPException(status_code=400,detail="Staff does not exists!")
    
    check_service = db.query(Service).filter(Service.id == bookingobject.service_id).first()

    if not check_service:

        raise HTTPException(status_code=400,detail="Service does not exists!")
    
    book = Booking(**bookingobject.model_dump())

    db.add(book)

    db.commit()

    db.refresh(book)

    return {"status":200,"message":"Booking Successfull","data":book}
    

@booking_router.get("/booking/{id}")
def get_all_bookings_per_user(id:str,db:Session=Depends(get_session)):

    bookings = (db.query(Booking).options(
        selectinload(Booking.services).load_only(Service.name),
        selectinload(Booking.staffs).load_only(Staff.name),
        selectinload(Booking.users).load_only(User.name),
        selectinload(Booking.salon).load_only(Salon.name),
    ).filter(Booking.user_id == id).all())

    if not bookings:

        raise HTTPException(status_code=400,detail="No Bookings found!")
    
    return {"status":200,"message":"Succesfully fetched Bookings","data":bookings}
     
    