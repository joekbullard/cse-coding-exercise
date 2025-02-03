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

    def calculate_offer_discount(self, basket_items: List[BasketItem]) -> Decimal:
        total_savings = 0
        for offer in self.offers:
            qualifying_items = [item for item in basket_items if item.name in offer.qualifying_items]

            if len(qualifying_items) >= offer.qualifying_quantity:
                # use floor division to return number of discounts to apply
                number_discounts = len(qualifying_items) // offer.qualifying_quantity

                offer_savings = number_discounts * -offer.discount_amount
                print(f"{str(offer).ljust(15)} {str(offer_savings).ljust(10)}")
                total_savings += offer_savings
        
        return total_savings