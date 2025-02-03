from shopping_basket import BasketItem, PriceType
from discounts import Offer
from decimal import Decimal

test_offers = [
    Offer(
        name='Coke two for £1',
        qualifying_items=['Coke'],
        qualifying_quantity=2, 
        discount_amount=Decimal('0.40')
    ),
    Offer(
        name='Beans 3 for 2',
        qualifying_items=['Beans'],
        qualifying_quantity=3, 
        discount_amount=Decimal('0.50')
    ),
]

test_items = [
    BasketItem(
        name="Beans", 
        unit_price=Decimal("0.50"), 
        price_type=PriceType.FIXED
    ),
    BasketItem(
        name="Beans", 
        unit_price=Decimal("0.50"), 
        price_type=PriceType.FIXED
    ),
    BasketItem(
        name="Beans", 
        unit_price=Decimal("0.50"), 
        price_type=PriceType.FIXED
    ),
    BasketItem(
        name="Coke",
        unit_price=Decimal("0.70"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="Coke",
        unit_price=Decimal("0.70"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="Oranges",
        unit_price=Decimal("1.99"),
        weight=Decimal("0.200"),
        price_type=PriceType.WEIGHED,
    ),
]
