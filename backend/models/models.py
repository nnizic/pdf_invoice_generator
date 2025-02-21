"""svi modeli za projekt"""

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    """korisnik"""

    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class LoginModel(UserModel):
    """model za logiranje u aplikaciju"""

    pass


class InvoiceModel(BaseModel):
    """model za račun"""

    customer_name: str = Field(..., min_length=3)
    date: datetime
    items: List[str]
    total: float


class InvoiceItem(BaseModel):
    """model za stavke računa"""

    name: str
    quantity: int
    price: float
    price: float
