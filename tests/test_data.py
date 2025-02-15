from shopping_basket import BasketItem, PriceType
from discounts import Offer, OfferType
from decimal import Decimal

test_offers = [
    Offer(
        name='Coke two for £1',
        qualifying_items=['Coke'],
        qualifying_quantity=2, 
        offer_type=OfferType.FIXED_ITEM,
        discount_amount=Decimal('0.40')
    ),
    Offer(
        name='Beans 3 for 2',
        qualifying_items=['Beans'],
        qualifying_quantity=3, 
        offer_type=OfferType.FIXED_ITEM,
        discount_amount=Decimal('0.50')
    ),
    Offer(
        name='3 Ales for £6',
        qualifying_items=['NEIPA', 'IPA', 'Golden Ale', 'Stout'],
        qualifying_quantity=3,
        offer_type=OfferType.FIXED_BUNDLE,
        discount_amount=Decimal('6.00')
    )
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
    BasketItem(
        name="IPA",
        unit_price=Decimal("2.99"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="NEIPA",
        unit_price=Decimal("2.39"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="Stout",
        unit_price=Decimal("2.29"),
        weight=Decimal("0.200"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="IPA",
        unit_price=Decimal("2.99"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="Stout",
        unit_price=Decimal("2.29"),
        price_type=PriceType.FIXED,
    ),
]
