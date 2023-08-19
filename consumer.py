import logging
import socket
import sys
import uuid
from typing import Generator

import orjson
from typing_extensions import Self

from configs import BOOTSTRAP_SERVERS, TOPIC_NAME
from db import Neo4jClient

from confluent_kafka import Consumer, KafkaError, KafkaException, Message


logging.basicConfig(stream=sys.stdout, level=logging.ERROR)


neo = Neo4jClient("bolt://localhost:7687", "neo4j", "password")


class CompanyConsumer:
    def __init__(self, config: dict | None = None):
        if config is None:
            config = {
                "bootstrap.servers": "plaintext://" + BOOTSTRAP_SERVERS,
                "group.id": TOPIC_NAME,
                "enable.auto.commit": False,
                "auto.offset.reset": "earliest",
                "group.instance.id": socket.gethostname() + str(uuid.uuid4()),
                # "security.protocol": "SSL",
                "on_commit": self.commit_callback,
                "client.id": socket.gethostname(),
                # "security.protocol": None
            }
        self.consumer = Consumer(config)
        logging.info("Initialized consumer: " + str(config))

    @staticmethod
    def commit_callback(kafka_error, topic_partition):
        response = {
            "kafka_error": kafka_error,
            "topic_partition": topic_partition
        }
        logging.info("Commit info: " + str(response))

    def for_topic(self, topic: str) -> Self:
        self.consumer.subscribe([topic])
        return self

    def messages(self) -> Generator[Message, None, None]:
        while True:
            msg: Message = self.consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    logging.error('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
                raise KafkaException(msg.error())
            else:
                yield msg

    def close(self):
        self.consumer.close()

    def poll(self, timeout: float):
        return self.consumer.poll(timeout)

    def commit(self, message: Message, asynchronous: bool = True):
        self.consumer.commit(message=message, asynchronous=asynchronous)


c = CompanyConsumer().for_topic(TOPIC_NAME)

try:
    for msg in c.messages():
        _msg = orjson.loads(msg.value().decode("utf-8"))
        logging.info(msg.key())
        neo.create(_msg)
        c.commit(message=msg, asynchronous=False)
except Exception as e:
    logging.error(str(e))
finally:
    c.close()
    exit(1)
