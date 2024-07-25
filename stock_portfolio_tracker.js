import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const Portfolio = () => {
  const [stocks, setStocks] = useState([]);
  const [totalValue, setTotalValue] = useState(0);

  useEffect(() => {
    axios.get('/api/portfolio').then(response => {
      setStocks(response.data.stocks);
      setTotalValue(response.data.total_value);
    });
  }, []);

  const stockData = {
    labels: stocks.map(stock => stock.symbol),
    datasets: [{
      label: 'Stock Value',
      data: stocks.map(stock => getCurrentPrice(stock.symbol) * stock.quantity),
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 1)',
    }]
  };

  return (
    <div>
      <h1>My Portfolio</h1>
      <h2>Total Value: ${totalValue.toFixed(2)}</h2>
      <Line data={stockData} />
      <ul>
        {stocks.map(stock => (
          <li key={stock.symbol}>
            {stock.symbol} - {stock.quantity} shares at ${stock.purchase_price} each
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Portfolio;
