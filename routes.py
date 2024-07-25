from flask import request, jsonify
from app import app, db
from models import Stock
import requests
import pandas as pd
import numpy as np

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    stocks = Stock.query.all()
    data = [{
        'symbol': stock.symbol,
        'quantity': stock.quantity,
        'purchase_price': stock.purchase_price
    } for stock in stocks]
    
    # Example: Adding simple analytics (total value)
    total_value = sum(stock.quantity * get_current_price(stock.symbol) for stock in stocks)
    
    return jsonify({
        'stocks': data,
        'total_value': total_value
    })

@app.route('/api/portfolio', methods=['POST'])
def add_stock():
    data = request.json
    new_stock = Stock(
        symbol=data['symbol'],
        quantity=data['quantity'],
        purchase_price=data['purchase_price']
    )
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({
        'symbol': new_stock.symbol,
        'quantity': new_stock.quantity,
        'purchase_price': new_stock.purchase_price
    })

@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    api_key = 'your_api_key_here'
    url = f'https://api.example.com/stock/{symbol}?apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
  // Example: Adding basic recommendation based on price trend
    current_price = data['currentPrice']
    recommendation = 'Hold'
    if current_price > get_average_price(symbol):
        recommendation = 'Sell'
    elif current_price < get_average_price(symbol):
        recommendation = 'Buy'
    
    data['recommendation'] = recommendation
    return jsonify(data)

def get_current_price(symbol):
    # Function to get current price from an API
    # Example implementation
    response = requests.get(f'https://api.example.com/stock/{symbol}/price')
    return response.json()['price']

def get_average_price(symbol):
    # Function to calculate average price (placeholder implementation)
    return 100.0  # Replace with actual logic
