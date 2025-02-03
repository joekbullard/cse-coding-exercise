from dataclasses import dataclass
from decimal import Decimal
from typing import List, Iterator
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
class OfferDiscount:
    '''
    return object from offer OfferCalculator.calculate_offers
    '''
    name: str
    discount_amount: Decimal

    def __str__(self):
        return f"{self.name.ljust(15)} {str(self.discount_amount).ljust(10)}"


@dataclass
class OfferCalculator:
    offers: List[Offer]

    def calculate_offers(self, items: List[BasketItem]) -> List[OfferDiscount]:
        return list(self._calculate_offer_discount(items))


    def _calculate_offer_discount(self, items: List[BasketItem]) -> Iterator[OfferDiscount]:
        for offer in self.offers:
            qualifying_items = [item for item in items if item.name in offer.qualifying_items]

            if len(qualifying_items) >= offer.qualifying_quantity:
                # use floor division to return number of discounts to apply
                number_discounts = len(qualifying_items) // offer.qualifying_quantity
                offer_savings = number_discounts * -offer.discount_amount
                yield OfferDiscount(name=offer.name, discount_amount=offer_savings)