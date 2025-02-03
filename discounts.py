from dataclasses import dataclass
from decimal import Decimal
from typing import List
from shopping_basket import BasketItem



@dataclass
class Offer:
    name: str
    qualifying_items: List[str]
    qualifying_quantity: int
    discount_amount: Decimal

    def __str__(self):
        return f"{self.name}"


@dataclass
class OfferCalculator:
    offers: List[Offer]