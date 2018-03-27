import requests
import datetime
import sqlite3
import time

def get_current_price():
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    return data['bpi']['USD']['rate_float']



conn = sqlite3.connect('btc_feed.db')
conn.execute('create table if not exists btc_price (date timestamp, price real)')


while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price = get_current_price()
    print(now, price)
    conn.execute("insert into btc_price (date, price) values ('{}',{})".format(now, price))
    time.sleep(2 * 60)

