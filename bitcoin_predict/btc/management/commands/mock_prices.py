import os
import csv
import gzip
import datetime
from btc.models import MockPrice
import requests
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Mocking Price data... saving to database')
        for x in range(1,32):
            if x < 10:
                day = '0' + str(x)
            else:
                day = str(x)
            d = '2018-01-' + day 
            p = MockPrice(date=d,price=100*x)
            p.save()
            
        self.stdout.write('Done!')
