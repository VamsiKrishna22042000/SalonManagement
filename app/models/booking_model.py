from sqlalchemy import Column,ForeignKey,Enum as SqlEnum,DateTime,String
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from ..config.db_connection import Base

import uuid

from enum import Enum

from datetime import datetime,timezone


class StatusEnum(str,Enum):

    booked = "Booked"
    completed="Completed"
    cancelled="Cancelled"
    rescheduled="Re-Scheduled"

class Booking(Base):

    __tablename__ = "Bookings"

    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)

    status=Column(SqlEnum(StatusEnum),nullable=False,default="Booked")
    date=Column(DateTime(timezone=True),nullable=False,default=datetime.now(timezone.utc))
    time=Column(String(20),nullable=False)

    user_id=Column(UUID(as_uuid=True),ForeignKey("Users.id"),nullable=False)
    service_id=Column(UUID(as_uuid=True),ForeignKey("Services.id"),nullable=False)
    staff_id=Column(UUID(as_uuid=True),ForeignKey("Staffs.id"),nullable=False)
    salon_id=Column(UUID(as_uuid=True),ForeignKey("Salons.id"),nullable=False)

    salon=relationship("Salon",back_populates="bookings")
    users=relationship("User",back_populates="bookings")
    services=relationship("Service",back_populates="bookings")
    staffs=relationship("Staff",back_populates="bookings")

