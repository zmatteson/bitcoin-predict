from django.test import TestCase
import datetime
# Create your tests here.
from bitcoin_rnn.models import FuturePrice
today = datetime.datetime.now()
yesterday = datetime.datetime.now()-datetime.timedelta(days=1)


class PriceTestCase(TestCase):
    def test_prices_have_a_date_and_price(self):
        """MockPrices have a price"""
        price_today = FuturePrice(price=100, date=today)
        price_yesterday = FuturePrice(price=200, date=yesterday)
        self.assertEqual(100, price_today.price)
        self.assertEqual(200, price_yesterday.price)