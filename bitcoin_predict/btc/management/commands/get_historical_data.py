import os
import csv
import gzip
import datetime
from btc.models import Price
import requests

url = 'http://api.bitcoincharts.com/v1/csv/btcalphaUSD.csv.gz'
filename = url.split('/')[-1]

if not os.path.exists(filename):
    print("Fetching historical data from api ...")
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fp:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                fp.write(chunk)

print("Adding price data to the database ...")
with gzip.open(filename, mode='rt') as fp:
    reader = csv.reader(fp)
    for line in reader:
        p = Price(date=datetime.datetime.fromtimestamp(int(line[0])),price=float(line[1]))
        p.save()
print("Done")
