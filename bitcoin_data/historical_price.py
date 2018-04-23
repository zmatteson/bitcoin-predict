import datetime as dt

import requests
import os
import gzip
import re
import requests
import urllib2
import sqlite3

API = 'http://api.bitcoincharts.com/v1/csv/'

# File name of coin base exchange data
FILE_NAME = 'coinbaseUSD.csv.gz'

def main():

	# Download csv file from API
	print 'Downloading csv '+ FILE_NAME + ' from API....'

	response = requests.get(API + FILE_NAME)

	with open(FILE_NAME, 'wb') as f:
		f.write(response.content)

	print 'Download complete!'

	# Open zip file and read csv dataset
	fi = gzip.open( FILE_NAME, 'rb')
	file_content = fi.read()
	to_db = []
	for l in file_content.split('\n'):
		record =  l.split(',')
		if len(record)==3:
			to_db.append((dt.datetime.fromtimestamp(int(record[0])), record[1]))
		# break
	fi.close()


	def create():
		# Create a table for data
	    try:
	        c.execute("""CREATE TABLE coinbase
	                 (timestamp, price)""")
	    except:
	        pass

	def drop():
		# Drop the table for inserting new data
	    try:
	    	print 'Deleting past records....'
	        c.execute("""DROP TABLE coinbase""")

	    except:
	        pass

	def insert():
		# Push data to table
	    c.executemany("""INSERT INTO coinbase (timestamp, price) VALUES (?, ?);""", to_db)
	    print 'Database updated!'

	db_path = r'coinbase.db'
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	drop()
	create()
	insert()
	conn.commit() #commit needed
	c.close()


if __name__ == '__main__':
	main()
