import os
import csv
import gzip
import datetime
from btc.models import MockPrice
import requests
from django.core.management.base import BaseCommand, CommandError
import random 

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Mocking Price data... saving to database')
        start_dt = datetime.datetime.now() - datetime.timedelta(days=90)
        end_dt = datetime.datetime.now()
        i = 7000
        for dt in daterange(start_dt, end_dt):
            p = MockPrice(date=dt,price=i)
            p.save()
            i += 100 - random.randint(-20,20)
        self.stdout.write('Done!')
