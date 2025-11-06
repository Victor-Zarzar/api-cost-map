from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class CostOfLivingCreate(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    category: Optional[str] = Field(default=None, max_length=100)
    amount: Decimal = Field(max_digits=12, decimal_places=2)
    currency: str = Field(min_length=3, max_length=3, default="BRL")
    city: Optional[str] = Field(default=None, max_length=120)
    country: Optional[str] = Field(default=None, max_length=120)


class CostOfLiving(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    category: Optional[str]
    amount: Decimal = Field(max_digits=12, decimal_places=2)
    currency: str
    city: Optional[str]
    country: Optional[str]
