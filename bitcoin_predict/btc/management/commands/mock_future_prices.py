import os
import csv
import gzip
import datetime
from btc.models import MockFuturePrice
import requests
from django.core.management.base import BaseCommand, CommandError
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Mocking Future Price data... saving to database')
        for x in range(1,32):
            if x < 10:
                day = '0' + str(x)
            else:
                day = str(x)
            d = '2018-01-' + day 
            p = MockFuturePrice(date=d,price=100*x - random.randint(-20,20))
            p.save()
            
        self.stdout.write('Done!')
