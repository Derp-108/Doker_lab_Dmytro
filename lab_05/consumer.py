from kafka import KafkaConsumer

topic = 'common'
bootstrap_servers = 'kafka:9092'

# Створення Kafka consumer
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

for message in consumer:
    # Отримання вмісту повідомлення
    content = message.value.decode('utf-8')

    # Виведення вмісту у термінал
    print(content)