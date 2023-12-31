import logging
import socket
import uuid
from typing import Generator

from admin import bootstrap
from confluent_kafka import Consumer, KafkaError, KafkaException, Message
from db import Neo4jClient
import schema
from settings import cfg
from typing_extensions import Self

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

neo = Neo4jClient(cfg.neo4j)


def make_config(topic_name, callback):
    return {
        "bootstrap.servers": "plaintext://" + cfg.redpanda.bootstrap_servers,
        "group.id": topic_name,
        "enable.auto.commit": False,
        "auto.offset.reset": "earliest",
        "group.instance.id": socket.gethostname() + str(uuid.uuid4()),
        # "security.protocol": "SSL",
        "on_commit": callback,
        "client.id": socket.gethostname(),
        # "security.protocol": None
    }


class RecordConsumer:
    def __init__(self, config: dict | None = None):
        if config is None:
            config = make_config(cfg.topics.RECORD, self.commit_callback)
        self.consumer = Consumer(config)
        logger.info("Initialized consumer: " + str(config))

    @staticmethod
    def commit_callback(kafka_error, topic_partition):
        response = {"kafka_error": kafka_error, "topic_partition": topic_partition}
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
                    logger.error("%% %s [%d] reached end at offset %d\n" % (msg.topic(), msg.partition(), msg.offset()))
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
    c = RecordConsumer().for_topic(cfg.redpanda.topic_name)

    try:
        for msg in c.messages():
            _msg = schema.LEICompany.model_validate_json(msg.value())
            logger.info(f"Consuming record: <{msg.key()=}>")
            neo.create(_msg.model_dump())
            c.commit(message=msg, asynchronous=False)
    except Exception as e:
        logger.error(str(e))
    finally:
        c.close()
        exit(1)
