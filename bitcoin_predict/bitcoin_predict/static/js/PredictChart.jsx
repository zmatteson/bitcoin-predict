import React, { Component } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const info = [65, 59, 80, 81, 56, 55, 45, 80, 100];
const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September'];

class PredictChart extends Component {
    state = {
        chartData: []
    };

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/apifutureprices/?format=json').then(result => {
            this.setState({ chartData: result.data.slice(155, 167) });
        });
    }

    render() {
        let datesRendered;
        let prices;
        let dates;
        if (this.state.chartData) {
            prices = this.state.chartData.map(dt => dt.price);
            dates = this.state.chartData.map(dt => dt.date);
            dates.sort();
            datesRendered = {
                labels: dates,
                datasets: [
                    {
                        label: 'BP Price',
                        backgroundColor: 'rgba(50,37,166,0.2)',
                        borderColor: 'rgba(50,37,166,1)',
                        borderWidth: 2,
                        hoverBackgroundColor: 'rgba(50,37,166,0.4)',
                        hoverBorderColor: 'rgba(50,37,166,1)',
                        data: prices
                    }
                ]
            };
        } else {
            datesRendered = {
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
        }
        return (
            <div>
                <h2>FUTURE PRICES: APRIL-MAY</h2>
                <Line data={datesRendered} />
            </div>
        );
    }
}

export default PredictChart;
