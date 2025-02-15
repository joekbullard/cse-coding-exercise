from shopping_basket import BasketItem, ShoppingBasket, PriceType
from discounts import Offer, OfferCalculator, OfferType
from decimal import Decimal

'''
Example script demonstrating shopping basket calculator
'''

offers = [
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

shopping_items = [
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
    BasketItem(
        name="IPA",
        unit_price=Decimal("2.99"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="Stout",
        unit_price=Decimal("2.29"),
        price_type=PriceType.FIXED,
    )
]


def main():

    line_break = '-' * 10
    shopping_basket = ShoppingBasket(shopping_items)
    offer_calculator = OfferCalculator(offers)
    subtotal = shopping_basket.subtotal()
    discounts = offer_calculator.calculate_offers(shopping_basket.items)
    total_savings = sum([discount.discount_amount for discount in discounts])
    total_to_pay = subtotal + total_savings
    

    print(shopping_basket)
    print(line_break)
    print(f"Sub-total: {subtotal}")
    print(line_break)
    print("Savings")
    [print(discount) for discount in discounts]
    print(f"Total savings: {total_savings}")
    print(line_break)
    print(f"Total to pay: {total_to_pay}\n")

if __name__ == "__main__":
    main()

