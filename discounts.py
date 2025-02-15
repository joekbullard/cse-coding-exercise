from dataclasses import dataclass
from decimal import Decimal
from typing import List, Iterator
from shopping_basket import BasketItem
from enum import Enum, auto


class OfferType(Enum):
    FIXED_BUNDLE = auto()
    FIXED_ITEM = auto()
    # could also have %age or threshold e.g.
    # PERCENTAGE = auto()
    # THRESHOLD = auto()


@dataclass
class Offer:
    name: str
    qualifying_items: List[str]
    qualifying_quantity: int
    offer_type: OfferType
    discount_amount: Decimal = None

    def __str__(self):
        return f"{self.name}"
    

""" For instances where multiple BasketItem in an offer you could have like this:
offer = Offer("3 Ales for £6", [golden_ale, ipa, neipa, stout], 3, DiscountType.FIXED_BUNDLE, 6.00)
"""

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
    offers: List[Offer]

    def calculate_offers(self, items: List[BasketItem]) -> List[OfferDiscount]:
        # Probably fine, although in cases where there an 
        sorted_items = sorted(items, key=lambda item: item.total_price)
        return list(self._calculate_offer_discount(sorted_items))


    def _calculate_offer_discount(self, items: List[BasketItem]) -> Iterator[OfferDiscount]:
        for offer in self.offers:

            qualifying_items = [item for item in items if item.name in offer.qualifying_items]
            if len(qualifying_items) >= offer.qualifying_quantity:

                # use floor division to return number of discounts to apply
                # this can go outside if statement as it applies to both types
                number_discounts = len(qualifying_items) // offer.qualifying_quantity

                if offer.offer_type == OfferType.FIXED_ITEM:
                    offer_savings = number_discounts * -offer.discount_amount

                elif offer.offer_type == OfferType.FIXED_BUNDLE:
                    total_items_in_bundle = number_discounts * offer.qualifying_quantity
                    offer_item_subtotal = 0
                    for item in qualifying_items[:total_items_in_bundle]:
                        offer_item_subtotal += item.total_price
                    offer_savings =  offer.discount_amount - offer_item_subtotal

                yield OfferDiscount(name=offer.name, discount_amount=offer_savings)

                    # cheapest_items = qualifying_items[:offer.qualifying_quantity]
                    # for _ in range(number_discounts):
                    #     total_price = sum([item.price for item in cheapest_items]) 
                    #     saving =  offer.discount_amount - total_price
                    # yield OfferDiscount(name=offer.name, discount_amount=saving)