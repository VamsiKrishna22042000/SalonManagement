from pydantic import BaseModel

from datetime import datetime

import uuid

from enum import Enum

from typing import Optional


class StatusEnum(str,Enum):
    booked = "Booked"
    completed="Completed"
    cancelled="Cancelled"
    rescheduled="Re-Scheduled"


class BookingP(BaseModel):
    user_id:uuid.UUID
    staff_id:uuid.UUID
    salon_id:uuid.UUID
    service_id:uuid.UUID
    date:datetime
    time:str
    status:StatusEnum

    class Config:

        from_attributes:True

class BokkingResponse(BookingP):
    id:uuid.UUID

    class Config:

        from_attributes:True