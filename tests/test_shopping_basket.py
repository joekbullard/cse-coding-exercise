import unittest
from decimal import Decimal
from test_data import test_items
from shopping_basket import BasketItem, ShoppingBasket, PriceType


class TestBasketItem(unittest.TestCase):
    def test_fixed_price_item(self):
        """Test total price calculation for fixed price items."""
        item = BasketItem(
            name="Coke",
            unit_price=Decimal("0.70"),
            quantity=3,
            price_type=PriceType.FIXED,
        )
        self.assertEqual(item.total_price, Decimal("2.10"))

    def test_weighed_price_item(self):
        item = BasketItem(
            name="Oranges",
            unit_price=Decimal("1.99"),
            weight=Decimal("0.200"),
            price_type=PriceType.WEIGHED,
        )
        self.assertEqual(item.total_price, Decimal("0.40"))


class TestShoppingBasket(unittest.TestCase):
    def setUp(self):
        "used data from exercise sheet"
        self.test_items = test_items

    def test_subtotal(self):
        basket = ShoppingBasket(self.test_items)
        self.assertEqual(basket.subtotal(), Decimal("16.25"))


if __name__ == "__main__":
    unittest.main()
