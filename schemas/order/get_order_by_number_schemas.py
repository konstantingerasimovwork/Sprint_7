from pydantic import BaseModel
from typing import Dict, List, Any


class GetSchema(BaseModel):

    order: Dict[str, Any]

class GetOrderSchema(BaseModel):

    id: int
    firstName: str
    lastName: str
    address: str
    metroStation: str
    phone: str
    rentTime: int
    deliveryDate: str
    track: int
    color: list[str]
    comment: str
    cancelled: bool
    finished: bool
    inDelivery: bool
    createdAt: str
    updatedAt: str
    status: int


class ErrorSchema(BaseModel):

    message: str
