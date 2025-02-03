from shopping_basket import BasketItem, PriceType
from decimal import Decimal

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
