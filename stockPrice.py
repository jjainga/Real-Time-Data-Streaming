from confluent_kafka import Producer
import requests
import time
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

API_KEY = os.getenv('APACHE_VANTAGE_KEY')
STOCK_SYMBOL = 'AAPL'

producer_conf = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(producer_conf)

tech_stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'FB', 'NVDA', 'ADBE', 'CRM', 'TSM', 'PYPL', 'INTC', 'CSCO', 'ASML', 'AVGO', 'TXN', 'QCOM', 'NFLX', 'AMAT', 'AMD', 'BIDU', 'JD']


def get_stock_price(symbol):
    try:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        stock_price = float(data['Global Quote']['05. price'])

        return stock_price
    except Exception as e:
        print(f'Error getting stock price for {symbol}: {e}')
        return None

while True:
    for stock in tech_stock_symbols:
        stock_price = get_stock_price(stock)
        if stock_price is not None:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{stock},{stock_price},{current_time}".encode()
            try:
                producer.produce('stock_prices', message)
                producer.flush()
            except Exception as e:
                print(f'Error producing message for {stock}: {e}')
        time.sleep(15)

