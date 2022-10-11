from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'logging.post.like',
    bootstrap_servers=['192.168.197.10:9092']
)

print('[begin] get consumer list')

for message in consumer:
    print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" % ( message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8') ))

print('[end] get consumer list')