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
We used the Django framework(with the addition of django-webpack-loader and webpack-bundle-tracker apps) as a means to connect our backend database to our front end React-app. Webpack-bundle-tracker is used to emit necessary data from the webpack bundles for  django-webpack-loader to consume that data.
- React: 
    Used React v3 for our front end, as well as with Chart.js to render our api data into charts and allow our charts to be animated. Axios was imported for our GET requests to our api. This allowed us to bring in data and use the most recent subset to continuously update our charts according to the new data brought into the apis. There were three main components: the header, the current chart (the first chart), the past chart (the second chart), the future predictions chart (the third chart). These three were rendered onto the landing page of the app, making it a one-page web application.
- Keras using Tensorflow: 

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


