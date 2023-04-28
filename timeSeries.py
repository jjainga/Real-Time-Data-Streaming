import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Set up the MySQL connection
cnx = mysql.connector.connect(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('database'))

def plot_top_five_stocks():
    cursor = cnx.cursor()

    query = """
        SELECT symbol, price, datetime
        FROM stock_prices
        WHERE (symbol, datetime) IN (
            SELECT symbol, MAX(datetime)
            FROM stock_prices
            GROUP BY symbol
            ORDER BY MAX(price) DESC
        )
        ORDER BY datetime ASC;
        LIMIT 5
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    # Create a dictionary to hold the data for each stock
    stock_data = {}

    # Iterate over the rows and populate the dictionary
    for row in rows:
        symbol = row[0]
        datetime_str = str(row[2])
        price = row[1]

        if symbol not in stock_data:
            stock_data[symbol] = {'x': [], 'y': []}

        stock_data[symbol]['x'].append(datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S'))
        stock_data[symbol]['y'].append(price)

    fig, ax = plt.subplots()

    # Plot the data for each stock
    for symbol, data in stock_data.items():
        ax.plot(data['x'], data['y'], label=symbol)

    ax.set_title('Top 5 Highest Price Stocks')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    cursor.close()
    return fig

# Plot the top 5 highest price stocks
plot_top_five_stocks()
plt.show()
