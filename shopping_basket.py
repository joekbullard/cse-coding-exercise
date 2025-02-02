from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from enum import Enum

class PriceType(Enum):
    FIXED = 0
    WEIGHED = 1

@dataclass
class BasketItem:
    name: str
    unit_price: Optional[Decimal]
    price_type: PriceType = 0
    weight: Optional[Decimal] = None
    quantity: int = 1
    