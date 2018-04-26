# README

Web App: Bitcoin Predict
================

Bitcoin Predict is a new, web application that displays current bitcoin prices and utilize deep learning neural networks to predict future bitcoin prices. The first chart shows the most recent collected data, the last 30 days specifically. The second chart shows past bitcoin price data, with an interactive menu for you to load data according to one of the past ones, up to three months before. The last chart shows our predictions for the upcoming month of bitcoin prices.

What We Learned
---------------
Each team member took on one large technology to learn. We used React for the front end, machine learning (using tensorflow) to create future prediction data for bitcoin prices, sqlite3 as our database, and Django to be able to encapsulate our application.

Requirements
---------------
All dependencies found in **bitcoin_predict/package.json** and **bitcoin_predict/bitcoin_predict/settings.py** under "INSTALLED_APPS." Recommended: using a virtualenv

Structure of System
-------------------
- Django: 

- React: 
We used React v3 for the front end. 
- Keras using Tensorflow: 
    - Keras.model.Sequential, Keras.model.layers.Dense, Keras.model.layers.LTSM to build the ML model
    - Kaggle BTC Historical Data to train the model
- Historical Price API:
Download Bitcoin price csv data zip file prom API http://api.bitcoincharts.com/v1/csv/
    - create coinbase.db to store historical Bitcoin prices extracted from the csv dataset file
    - delete the past records in the existing Bitcoin price table and update with new data
    - System requirements:
      * python 2.7
      * matplotlib (py lib)
      * requests (py lib)
      * numpy (py lib)
      * sqlite3

- Algorithms: recurrent neural network


