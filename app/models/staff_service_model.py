from sqlalchemy import Column,Integer,String,Float,Text,ForeignKey,ARRAY

from ..config.db_connection import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid

class Salon(Base):

    __tablename__ = "Salons"

    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    name=Column(String(100),nullable=False)
    address=Column(Text,nullable=False)
    city=Column(Text,nullable=True)
    pincode=Column(String(6),nullable=True)
    country=Column(String(100),nullable=False)

    services= relationship("Service",back_populates="salon")
    staffs= relationship("Staff",back_populates="salon")
    users = relationship("User",back_populates="salon")
    bookings = relationship("Booking",back_populates="salon")

class Service(Base):
    
    __tablename__ = "Services"

    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    name=Column(String(200),nullable=False)
    price=Column(Float,nullable=False)
    description=Column(Text,nullable=True)
    salon_id=Column(UUID(as_uuid=True),ForeignKey("Salons.id"),nullable=False)

    salon = relationship("Salon",back_populates="services")
    bookings = relationship("Booking",back_populates="services")

class Staff(Base):

    __tablename__="Staffs"

    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    name=Column(String(200),nullable=False)
    email=Column(String(100),unique=True,index=True,nullable=False)
    expirence=Column(Integer,nullable=False)
    slots=Column(ARRAY(String(20)),nullable=False,default=["9:00AM-10:00AM","10:00AM-11:00AM","11:00AM-12:00PM","12:00PM-1:00PM","1:00PM-2:00PM","2:00PM-3:00PM","3:00PM-4:00PM","4:00PM-5:00PM","5:00PM-6:00PM","6:00PM-7:00PM","7:00PM-8:00PM","8:00PM-9:00PM"])
    service_specality=Column(ARRAY(String(150)),nullable=False)
    salon_id=Column(UUID(as_uuid=True),ForeignKey("Salons.id"),nullable=False)
    rating=Column(Float,nullable=True,default=0.0)

    salon=relationship("Salon",back_populates="staffs")
    bookings = relationship("Booking",back_populates="staffs")
    
