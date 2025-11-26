from sqlalchemy import Column,String,Text,String,ForeignKey,Enum as SqlEnum
from sqlalchemy.dialects.postgresql import UUID

from enum import Enum

from sqlalchemy.orm import relationship

from ..config.db_connection import Base

import uuid


class RoleEnum(str,Enum):
    user="user"
    admin="admin"
    staff="staff"


class User(Base):

    __tablename__="Users"
    
    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    name=Column(String(200),nullable=False)
    email=Column(String(200),unique=True,index=True,nullable=False)
    password=Column(String(300),nullable=False)
    number=Column(String(10),nullable=False)
    address=Column(Text,nullable=True)
    role=Column(SqlEnum(RoleEnum),nullable=False,default="user")
    salon_id=Column(UUID(as_uuid=True),ForeignKey("Salons.id"),nullable=False)

    salon=relationship("Salon",back_populates="users")
    bookings=relationship("Booking",back_populates="users")