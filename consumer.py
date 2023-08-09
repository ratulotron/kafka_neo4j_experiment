import json
import uuid

from kafka import KafkaConsumer

from app import BOOTSTRAP_SERVERS, TOPIC_NAME
from pprint import pprint

from db import Neo4jClient


class Consumer:
    def __init__(self, brokers, topic, driver, group_id=None):
        self.driver = driver
        if group_id is None:
            # group_id = str(uuid.uuid4())
            group_id = topic
        self.consumer = KafkaConsumer(
            topic,
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            bootstrap_servers=brokers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        )

        self.consumer.subscribe([topic])

    def run(self):
        while True:
            for message in self.consumer:
                pprint(message.value)
                self.driver.create(message.value)
                self.consumer.commit()
            self.consumer.commit()

    def close(self):
        self.consumer.close()


neo = Neo4jClient("bolt://localhost:7687", "neo4j", "password")
consumer = Consumer(BOOTSTRAP_SERVERS, TOPIC_NAME, neo)
consumer.run()
