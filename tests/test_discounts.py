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
        savings = offer_caulculator.calculate_offer_discount(
            basket_items=self.test_items
        )
        self.assertEqual(savings, Decimal("-0.90"))
