from pydantic import BaseModel, Field
from datetime import date
from typing import List

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class InvoiceCreate(BaseModel):
    customer_name: str = Field(..., min_length=3)
    date: date
    items: List[str]
    total: float

