// @flow

import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Landing from './Landing';
import Header from './Header';

const FourOhFour = () => <h1>404</h1>;

const App = () => (
	<BrowserRouter>
		<div className="app">
			<Header />
			<div>
				<Switch>
					<Route exact path="/" component={Landing} />
					<Route component={FourOhFour} />
				</Switch>
			</div>
		</div>

	</BrowserRouter>
);

export default App;
