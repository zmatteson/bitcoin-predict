# Extracting Bitcoin price data

  ## historical_price.py:
    - download Bitcoin price csv data zip file prom API http://api.bitcoincharts.com/v1/csv/
    - create coinbase.db to store historical Bitcoin prices extracted from the csv dataset file
    - delete the past records in the existing Bitcoin price table and update with new data
    - System requirements:
      * python 2.7
	    * matplotlib (py lib)
	    * requests (py lib)
    	* numpy (py lib)
    	* sqlite3
