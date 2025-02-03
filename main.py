from shopping_basket import BasketItem, ShoppingBasket, PriceType
from discounts import Offer, OfferCalculator
from decimal import Decimal

'''
Example script demonstrating shopping basket calculator
'''

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
        name="Coke",
        unit_price=Decimal("0.70"),
        price_type=PriceType.FIXED,
    ),
    BasketItem(
        name="Onions",
        unit_price=Decimal("0.29"),
        weight=Decimal("0.400"),
        price_type=PriceType.WEIGHED,
    ),
]


offers = [
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


def main():

    line_break = '-' * 10

    shopping_basket = ShoppingBasket(shopping_items)
    offer_calculator = OfferCalculator(offers)
    subtotal = shopping_basket.subtotal()
    

    print(shopping_basket)
    print(line_break)
    print(f"Sub-total: {subtotal}")
    print(line_break)
    print("Savings")
    total_savings = offer_calculator.calculate_offer_discount(shopping_basket.items)
    if total_savings < 0:
        print(f"Total savings {str(total_savings)}")
    total_to_pay = subtotal + total_savings
    print(line_break)
    print(f"Total to pay: {total_to_pay}\n")

if __name__ == "__main__":
    main()

