// @flow

import React from 'react';
import styled from 'styled-components';

const Image = styled.img`
	width: 35%;
	float: left;
	margin-right: 10px;
`;

const Header = () => (
	<header>
		<Image alt={`BP Logo`} src={'/public/img/BPlogo.png'} />
		<h2><u>About</u></h2>
		<h2><u>Current Price</u></h2>
		<h2><u>Past Prices</u></h2>
		<h2><u>Future Price Prediction</u></h2>
	</header>
);

export default Header;
