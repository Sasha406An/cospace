from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True

class ResourceCreate(BaseModel):
    name: str
    type: str
    price: float

class ResourceResponse(BaseModel):
    id: int
    name: str
    type: str
    price: float
    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    user_id: int
    resource_id: int
    start_time: datetime
    end_time: datetime

class BookingResponse(BaseModel):
    id: int
    user_id: int
    resource_id: int
    start_time: datetime
    end_time: datetime
    class Config:
        from_attributes = True