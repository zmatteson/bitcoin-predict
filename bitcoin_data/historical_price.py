import os
import csv
import gzip
import datetime

import requests
import psycopg2



url = 'http://api.bitcoincharts.com/v1/csv/btcalphaUSD.csv.gz'
filename = url.split('/')[-1]

if not os.path.exists(filename):
    print("Fetching historical data from api ...")
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fp:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                fp.write(chunk)


conn = psycopg2.connect("dbname='btc_price' user='root' host='localhost' password='root'")

cur = conn.cursor()
cur.execute('drop table if exists btc_price')
cur.execute('create table btc_price (date timestamp, price real)')

print("Adding price data to the database ...")
with gzip.open(filename, mode='rb') as fp:
    reader = csv.reader(fp)
    for line in reader:
        date = datetime.datetime.fromtimestamp(int(line[0]))
        value = float(line[1])
        cur.execute('insert into btc_price (date, price) values (%s,%s)', args=(date, value))
        
conn.commit()
print("Done")
