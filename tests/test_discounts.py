from decimal import Decimal
import unittest
from test_data import test_items, test_offers
from discounts import OfferCalculator


class TestOfferCalculator(unittest.TestCase):
    def setUp(self):
        "used data from exercise sheet"
        self.test_items = test_items
        self.test_offers = test_offers

    def test_offer_discount(self):
        offer_caulculator = OfferCalculator(offers=self.test_offers)
        discounts = offer_caulculator.calculate_offers(
            items=self.test_items
        )
        total_savings = sum([discount.discount_amount for discount in discounts])
        self.assertEqual(total_savings, Decimal("-0.90"))

if __name__ == "__main__":
    unittest.main()