from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Helper function to get current stock price
def get_current_price(symbol):
    api_key = 'your_api_key_here'
    url = f'https://api.example.com/stock/{symbol}?apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data.get('currentPrice', 0.0)

# API Route to get portfolio
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    stocks = Stock.query.all()
    portfolio = [{
        'symbol': stock.symbol,
        'quantity': stock.quantity,
        'purchase_price': stock.purchase_price,
        'current_price': get_current_price(stock.symbol)
    } for stock in stocks]

    total_value = sum(stock['quantity'] * stock['current_price'] for stock in portfolio)
    return jsonify({
        'stocks': portfolio,
        'total_value': total_value
    })

# API Route to add a stock
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

# API Route to get stock data
@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    current_price = get_current_price(symbol)
    recommendation = 'Hold'
    # Simple recommendation logic based on price (replace with actual logic)
    if current_price > 100:
        recommendation = 'Sell'
    elif current_price < 50:
        recommendation = 'Buy'
    
    return jsonify({
        'symbol': symbol,
        'current_price': current_price,
        'recommendation': recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)
