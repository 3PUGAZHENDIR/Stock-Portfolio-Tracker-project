

Stock Portfolio Tracker

 Overview

The Stock Portfolio Tracker is a web application that allows users to manage and track their stock investments. Users can add, remove, and view stocks in their portfolio, get real-time updates on stock prices, and receive recommendations based on market data.

**Features:**
- Add and remove stocks from your portfolio
- View real-time stock prices and portfolio value
- Get personalized recommendations based on stock trends
- Interactive dashboard with historical performance charts
- Custom alerts for stock price changes

Technologies Used

- **Frontend:** React
- **Backend:** Flask
- **Database:** SQLite
- **APIs:** [Alpha Vantage](https://www.alphavantage.co) 

Installation

 Frontend

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/stock-portfolio-tracker.git
    ```

2. Navigate to the `frontend` directory:

    ```bash
    cd stock-portfolio-tracker/frontend
    ```

3. Install the dependencies:

    ```bash
    npm install
    ```

4. Start the development server:

    ```bash
    npm start
    ```

 Backend

1. Navigate to the `backend` directory:

    ```bash
    cd stock-portfolio-tracker/backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python app.py
    ```

5. Start the Flask server:

    ```bash
    flask run
    ```

Usage

1. **Adding Stocks:** Use the "Add Stock" form on the dashboard to enter stock symbol, quantity, and purchase price.
2. **Removing Stocks:** Use the "Remove" button next to each stock entry in the portfolio list.
3. **Viewing Stock Data:** Click on a stock symbol to see real-time data and recommendations.
4. **Custom Alerts:** Set up alerts to receive notifications about stock price changes.
5. 
 API Endpoints

- **GET** `/api/portfolio` - Retrieve the current portfolio.
- **POST** `/api/portfolio` - Add a new stock to the portfolio.
- **GET** `/api/stock/<symbol>` - Get real-time data and recommendations for a specific stock.

- 📬 Contact

For any questions or feedback, feel free to reach out to me at pugal06012002@gmail.com.



