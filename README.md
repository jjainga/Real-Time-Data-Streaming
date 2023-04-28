Real-Time Data Streaming
This project demonstrates a real-time data streaming pipeline that retrieves stock prices from the Alpha Vantage API, writes the data to a Kafka topic using the Confluent Kafka Python library, and consumes the data from the topic to display the top 5 highest-priced stocks in a Matplotlib graph.

Requirements
To run this project, you will need:

Python 3.7 or later
A MySQL database
An Alpha Vantage API key
Apache Kafka and ZooKeeper
The Confluent Kafka Python library
Matplotlib
Installation
Clone this repository: git clone https://github.com/jjainga/Real-Time-Data-Streaming
Install the required Python packages: pip install -r requirements.txt
Set the environment variables for your MySQL database and Alpha Vantage API key in a .env file in the project root directory. Example:
makefile
Copy code
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=mydatabase
DB_USER=myusername
DB_PASSWORD=mypassword
ALPHA_VANTAGE_API_KEY=12345
Configure Apache Kafka and ZooKeeper. See the Kafka documentation for instructions.
Create a Kafka topic for the stock prices. Example:
css
Copy code
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stock-prices
Usage
Run the producer to retrieve the stock prices and write them to the Kafka topic: python producer.py
Run the consumer to read the data from the Kafka topic and display the top 5 highest-priced stocks in a Matplotlib graph: python consumer.py
The consumer script will continue to run and update the graph every minute as new data is produced to the Kafka topic by the producer.

License
This project is licensed under the MIT License. See the LICENSE file for details.