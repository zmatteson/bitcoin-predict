from django.test import TestCase
import datetime
# Create your tests here.
from btc.models import Price, MockPrice, MockFuturePrice

today = datetime.datetime.now()
yesterday = datetime.datetime.now()-datetime.timedelta(days=1)


class PriceTestCase(TestCase):
    def test_prices_have_a_date_and_price(self):
        """MockPrices have a price"""
        price_today = Price(price=100, date=today)
        price_yesterday = Price(price=200, date=yesterday)
        self.assertEqual(100, price_today.price)
        self.assertEqual(200, price_yesterday.price)

class MockPriceTestCase(TestCase):
    def test_prices_have_a_date_and_price(self):
        """MockPrices have a price"""
        price_today = MockPrice(price=100, date=today)
        price_yesterday = MockPrice(price=200, date=yesterday)
        self.assertEqual(100, price_today.price)
        self.assertEqual(200, price_yesterday.price)

class MockFuturePriceTestCase(TestCase):
    def test_prices_have_a_date_and_price(self):
        """Prices have a price"""
        price_today = MockFuturePrice(price=100, date=today)
        price_yesterday = MockFuturePrice(price=200, date=yesterday)
        self.assertEqual(100, price_today.price)
        self.assertEqual(200, price_yesterday.price)