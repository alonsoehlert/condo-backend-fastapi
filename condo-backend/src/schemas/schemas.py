from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class Unit(BaseModel):
    id: Optional[str] = None
    owner: str
    condo_name: str
    address: str

    class Config:
        orm_mode = True

class Tenant(BaseModel):
    #id: Optional[int] = None
    name: str
    age: int
    gender: str
    phone: int
    email: str

    class Config:
        orm_mode = True


class UnitExpense(BaseModel):
    id: Optional[int] 
    description: str
    type_expense: str
    amount: float
    due_date: datetime
    payment_status: str
    unit_id: Optional[int]

    class Config:
        orm_mode = True

 



   





