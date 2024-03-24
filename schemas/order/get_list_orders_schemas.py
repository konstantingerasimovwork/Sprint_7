from pydantic import BaseModel
from typing import Dict, List, Any


class GetSchema(BaseModel):

    orders: List[Dict[str, Any]]
    pageInfo: Dict[str, Any]
    availableStations: List[Dict[str, Any]]


class GetOrdersSchema(BaseModel):

    id: Any
    courierId: Any
    firstName: Any
    lastName: Any
    address: Any
    metroStation: Any
    phone: Any
    rentTime: Any
    deliveryDate: Any
    track: Any
    color: Any
    comment: Any
    createdAt: Any
    updatedAt: Any
    status: Any
