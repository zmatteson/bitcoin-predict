// @flow

import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import About from './About';
import Header from './Header';

const FourOhFour = () => <h1>404</h1>;

const App = () => (
	<BrowserRouter>
		<div className="app">
			<Header />
			<Switch>
				<Route exact path="/" component={About} />
				<Route component={FourOhFour} />
			</Switch>
		</div>
	</BrowserRouter>
);

export default App;
