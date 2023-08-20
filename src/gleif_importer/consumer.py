import logging
import socket
import sys
import uuid
from typing import Generator
from typing_extensions import Self

from admin import bootstrap
from schema import Schema
from settings import cfg
from db import Neo4jClient

from confluent_kafka import Consumer, KafkaError, KafkaException, Message


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

neo = Neo4jClient(cfg.neo4j)


class CompanyConsumer:
    def __init__(self, config: dict | None = None):
        if config is None:
            config = {
                "bootstrap.servers": "plaintext://" + cfg.redpanda.bootstrap_servers,
                "group.id": cfg.redpanda.topic_name,
                "enable.auto.commit": False,
                "auto.offset.reset": "earliest",
                "group.instance.id": socket.gethostname() + str(uuid.uuid4()),
                # "security.protocol": "SSL",
                "on_commit": self.commit_callback,
                "client.id": socket.gethostname(),
                # "security.protocol": None
            }
        self.consumer = Consumer(config)
        logger.info("Initialized consumer: " + str(config))

    @staticmethod
    def commit_callback(kafka_error, topic_partition):
        response = {
            "kafka_error": kafka_error,
            "topic_partition": topic_partition
        }
        logger.info("Commit info: " + str(response))

    def for_topic(self, topic: str) -> Self:
        self.consumer.subscribe([topic])
        logger.info(f"Subscribed to topic {topic}")
        return self

    def messages(self) -> Generator[Message, None, None]:
        while True:
            __msg: Message = self.consumer.poll(timeout=1.0)
            if __msg is None:
                continue
            if __msg.error():
                if __msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    logger.error('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
                elif __msg.error():
                    raise KafkaException(__msg.error())
                raise KafkaException(__msg.error())
            else:
                yield __msg

    def close(self):
        self.consumer.close()

    def poll(self, timeout: float):
        return self.consumer.poll(timeout)

    def commit(self, message: Message, asynchronous: bool = True):
        self.consumer.commit(message=message, asynchronous=asynchronous)


if __name__ == "__main__":
    bootstrap()
    c = CompanyConsumer().for_topic(cfg.redpanda.topic_name)

    try:
        for msg in c.messages():
            _msg = Schema.model_validate_json(msg.value())
            logger.info(f"Consuming record: <{msg.key()}> \n {_msg.model_dump()}")
            neo.create(_msg.model_dump())
            c.commit(message=msg, asynchronous=False)
    except Exception as e:
        logger.error(str(e))
    finally:
        c.close()
        exit(1)
