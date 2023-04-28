from confluent_kafka import Consumer, KafkaError

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
consumer.subscribe(['stock_prices'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print(f'End of partition reached {msg.topic()}/{msg.partition()}')
        else:
            print(f'Error while polling message: {msg.error()}')
    else:
        print(f'Received message: {msg.value().decode()}')

