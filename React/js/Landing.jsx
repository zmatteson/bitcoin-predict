// @flow

import React from 'react';
import Chart from './Chart';

const Landing = () => (
	<div className="landing">
		<h1> -</h1>
		<h1> -</h1>
		<h1> -</h1>
		<h1> -</h1>
		<h1> -</h1>
		<h1> -</h1>
		<h1>ABOUT</h1>
		<p>
			Bitcoin Predict is a new, web application that displays current bitcoin prices and utilize
			deep learning neural networks to predict future bitcoin prices, which will then be displayed to the user
			on a line graph.
		</p>
		<Chart />
		<Chart />
		<Chart />
	</div>
);

export default Landing;
