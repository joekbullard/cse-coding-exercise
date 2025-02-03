from decimal import Decimal
import unittest
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

if __name__ == '__main__':
    unittest.main()
