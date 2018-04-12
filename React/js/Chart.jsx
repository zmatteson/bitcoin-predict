// @flow

import React, { Component } from 'react';
import styled from 'styled-components';

const Wrapper = styled.div`
	width: 100%;
	border: 2px solid #333;
	border-radius: 4px;
	margin-bottom: 25px;
	padding-right: 10px;
	overflow: hidden;
	color: black;
	text-decoration: none;
`;

class Chart extends Component {
	state = {
		chartMonth: ''
	};
	handleChartChange = (event: SyntheticKeyboardEvent & { target: HTMLInputElement }) => {
		this.setState({ chartMonth: event.target.value });
	};
	render() {
		return (
			<Wrapper>
				<div>
					<h1>February</h1>
					<img alt={'Sample Chart'} src={'/public/img/SampleChart.png'} />
				</div>
			</Wrapper>
		);
	}
}

export default Chart;
