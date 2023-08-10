from app import BOOTSTRAP_SERVERS, TOPIC_NAME
from pprint import pprint

from db import Neo4jClient

from confluent_kafka import Consumer


neo = Neo4jClient("bolt://localhost:7687", "neo4j", "password")

c = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': TOPIC_NAME,
    'auto.offset.reset': 'earliest'
})

c.subscribe([TOPIC_NAME])


while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    # print('Received message: {}'.format(msg.value().decode('utf-8')))
    pprint(msg.value)
    neo.driver.create(msg.value)
    c.commit()

c.close()
