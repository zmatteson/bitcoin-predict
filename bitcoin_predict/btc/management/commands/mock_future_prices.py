import os
import csv
import gzip
import datetime
from btc.models import MockFuturePrice
import requests
from django.core.management.base import BaseCommand, CommandError
import random

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Mocking Future Price data... saving to database')

        start_dt = datetime.datetime.now() - datetime.timedelta(days=97)
        end_dt = datetime.datetime.now() + datetime.timedelta(days=7)
        i = 7000
        for dt in daterange(start_dt, end_dt):
            p = MockFuturePrice(date=dt,price=i - random.randint(-30,30))
            p.save()
            i += 100 - random.randint(-30,30)
        self.stdout.write('Done!')
