// @flow

import React from 'react';
import CurrentChart from './CurrentChart';
import PastChart from './PastChart';
import PredictChart from './PredictChart';

const Landing = () => (
    <div className="landing">
        <CurrentChart />
        <PastChart />
        <a href="http://127.0.0.1:8000/">January</a>
        <a href="http://127.0.0.1:8000/">February</a>
        <a href="http://127.0.0.1:8000/">March</a>
        <PredictChart />
        <h1><b><u>ABOUT</u></b></h1>
        <p>
            Bitcoin Predict is a new, web application that displays current bitcoin prices and utilize
            deep learning neural networks to predict future bitcoin prices. The first chart shows the most recent collected data, the last 30 days specifically. The second chart shows past bitcoin price data, with an interactive menu for you to load data according to one of the past ones, up to three months before. The last chart shows our predictions for the upcoming month of bitcoin prices.

        </p>
        <a href="https://github.com/zmatteson/bitcoin-predict">Github Repository Here</a>
    </div>
);

export default Landing;
