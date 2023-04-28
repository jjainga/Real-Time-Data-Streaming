from confluent_kafka import Producer
import requests
import time
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv('APACHE_VANTAGE_KEY')
STOCK_SYMBOL = 'AAPL'

producer_conf = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(producer_conf)

def get_stock_price():
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={STOCK_SYMBOL}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    # print(data['Global Quote']['05. price'])
    if 'Global Quote' in data:
        stock_price = float(data['Global Quote']['05. price'])
        time.sleep(10)
        return stock_price
    else:
        print('Error: response missing required data')
        print(data)
        return None

while True:
    stock_price = get_stock_price()
    producer.produce('stock_prices', str(stock_price).encode())
    producer.flush() #wait for message delivery
    time.sleep(5)
