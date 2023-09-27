from kafka import KafkaProducer

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send some messages
for i in range(10):
    message = f'message number {i}'
    print(f'Sending: {message}')
    producer.send('my_topic', message)

# Ensure all messages have been sent
producer.flush()

from kafka import KafkaConsumer

# Create an instance of the Kafka consumer
consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092')

# Receive messages
for message in consumer:
    print(f'Received: {message.value}')