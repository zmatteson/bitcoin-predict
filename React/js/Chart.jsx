import React from 'react';
import { Line } from 'react-chartjs-2';

const info = [65, 59, 80, 81, 56, 55, 45, 80, 100];
const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September'];

const data = {
	labels: months,
	datasets: [
		{
			label: 'My First dataset',
			backgroundColor: 'rgba(255,99,132,0.2)',
			borderColor: 'rgba(255,99,132,1)',
			borderWidth: 2,
			hoverBackgroundColor: 'rgba(255,99,132,0.4)',
			hoverBorderColor: 'rgba(255,99,132,1)',
			data: info
		}
	]
};

const Chart = () => ({
	displayName: 'BarExample',

	render() {
		return (
			<div>
				<h2>Line Graph Example</h2>
				<Line data={data} />
			</div>
		);
	}
});

export default Chart;
