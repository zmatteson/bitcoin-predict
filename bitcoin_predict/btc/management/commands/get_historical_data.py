import os
import csv
import gzip
import datetime
from btc.models import Price
import requests
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'http://api.bitcoincharts.com/v1/csv/btcalphaUSD.csv.gz'
        filename = url.split('/')[-1]

        if not os.path.exists(filename):
            self.stdout.write("Fetching historical data from api ...")
            r = requests.get(url, stream=True)
            with open(filename, 'wb') as fp:
                for chunk in r.iter_content(chunk_size=1024): 
                    if chunk:
                        fp.write(chunk)

        self.stdout.write("Adding price data to the database ...")
        with gzip.open(filename, mode='rt') as fp:
            reader = csv.reader(fp)
            for line in reader:
                p = Price(date=datetime.datetime.fromtimestamp(int(line[0])),price=float(line[1]))
                self.stdout.write("Adding", str(p), "to database")
                try:
                    p.save()
                except Exception:
                    self.stdout.write(Exception, "could not add", str(p), "to database")
                    continue
        self.stdout.write("Done")
