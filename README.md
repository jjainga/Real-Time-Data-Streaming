<h1>Real-Time Data Streaming</h1>
<br>
This project demonstrates a real-time data streaming pipeline that retrieves stock prices from the Alpha Vantage API, writes the data to a Kafka topic using the Confluent Kafka Python library, and consumes the data from the topic to display the top 5 highest-priced stocks in a Matplotlib graph.
<br>
<h5>Requirements</h5>
To run this project, you will need:
<br>
Python 3.7 or later
A MySQL database
An Alpha Vantage API key
Apache Kafka and ZooKeeper
The Confluent Kafka Python library
Matplotlib
<br>
<h5>Installation</h5>
Clone this repository: 
<br>
<code>git clone https://github.com/jjainga/Real-Time-Data-Streaming</code>
<br>
Install the required Python packages: 
<br>
<code>pip install -r requirements.txt</code>
Set the environment variables for your MySQL database and Alpha Vantage API key in a .env file in the project root directory. Example:
makefile
<br>
<h6>Copy code<h6>
<code>
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=mydatabase
DB_USER=myusername
DB_PASSWORD=mypassword
ALPHA_VANTAGE_API_KEY=12345
</code>
<br>
Configure Apache Kafka and ZooKeeper. See the Kafka documentation for instructions.
<br>
Create a Kafka topic for the stock prices. Example:
css
Copy code
<code>kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stock-prices</code>
<br>
<h5>Usage</h5>
<br>
Run the producer to retrieve the stock prices and write them to the Kafka topic: python stockPrice.py
<br>
Run the consumer to read the data from the Kafka topic and display the top 5 highest-priced stocks in a Matplotlib graph: python consumer.py
<br>
The consumer script will continue to run and update the graph every minute as new data is produced to the Kafka topic by the producer.
<br>
<h5>License</h5>
<br>
This project is licensed under the MIT License. See the LICENSE file for details.