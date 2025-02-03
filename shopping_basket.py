from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, List
from enum import Enum

TWOPLACES = Decimal("0.01")

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

    @property
    def total_price(self) -> Decimal:
        if self.price_type == PriceType.FIXED:
            return (self.quantity * self.unit_price).quantize(TWOPLACES)
        elif self.price_type == PriceType.WEIGHED:
            return (self.weight * self.unit_price).quantize(TWOPLACES)
        
    def __str__(self):
        return f"{self.name.ljust(10)} £{str(self.total_price).ljust(10)}"
        

@dataclass
class ShoppingBasket:
    items: List[BasketItem]

    def add_item(self, item: BasketItem) -> None:
        self.items.append(item)

    def remove_item(self) -> None:
        '''This is a placeholder method in the absence of a UI'''
        pass

    def subtotal(self) -> Decimal:
        return sum([item.total_price for item in self.items]).quantize(TWOPLACES)
    
    def __str__(self):
        return "\n".join([str(item) for item in self.items])
