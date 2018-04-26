// @flow

import React from 'react';
import CurrentChart from './CurrentChart';
import PastChart from './PastChart';
import PredictChart from './PredictChart';

const Landing = () => (
    <div className="landing">
        <CurrentChart />
        <PastChart />
        <PredictChart />
        <h1>ABOUT</h1>
        <p>
            Bitcoin Predict is a new, web application that displays current bitcoin prices and utilize
            deep learning neural networks to predict future bitcoin prices, which will then be displayed to the user
            on a line graph.
        </p>
    </div>
);

export default Landing;
