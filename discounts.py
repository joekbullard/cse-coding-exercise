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
    Return object from offer OfferCalculator.calculate_offers
    '''
    name: str
    discount_amount: Decimal

    def __str__(self):
        return f"{self.name.ljust(15)} {str(self.discount_amount).ljust(10)}"


@dataclass
class OfferCalculator:
    '''
    Given a list of BasketItems, Calculates Offers and returns a list of OfferDiscount
    Caveats
    - Multiple offers for the same items will be applied
    - Assumes positive number for discount amount
    
    O(n^2) - quadratic time
    Non performant e.g. 2x for loops embedded in each other
    
    1. for loop cycling through the offers
    2. filter cycling through the items for every offer
    
    I do not expect a customers basket to contain large amounts of items
    however if this code is reused for large catalogues instead of customer baskets
    we should consider making a more performant algorithm to avoid quadratic time
    
    A possible improvement could be to pass a filtered array of items into calculate_offers
    so that we only calculate offers on items that we know to have corresponding offers

    Also needs adjustment to facilitate dynamic discounting (e.g. ales offer which is not implemented)
    '''
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
