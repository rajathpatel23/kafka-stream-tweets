from kafka import KafkaConsumer
import json



if __name__ == '__main__':
    consumer = KafkaConsumer(
        'neurallink',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        message = message.value
        print(message)