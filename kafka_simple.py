from kafka import KafkaProducer, KafkaConsumer

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send messages
for i in range(10):
    message = f'message number {i}'
    print(f'Sending: {message}')
    message_bytes = message.encode('utf-8')
    producer.send('my_topic', message_bytes)

# Ensure all messages are sent
producer.flush()

# Create Kafka consumer
consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

# Receive messages
try:
    for i, message in enumerate(consumer):
        print(f'Received: {message.value.decode("utf-8")}')
        if i >= 9:
            break
finally:
    consumer.close()