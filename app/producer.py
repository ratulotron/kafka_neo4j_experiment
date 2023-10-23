import logging

from confluent_kafka import Producer
import schema
from settings import cfg

logger = logging.getLogger(__name__)


class CompanyProducer:
    def __init__(self, config: dict | None = None):
        if config is None:
            config = {
                # "transactional.id": "gleif",
                "client.id": "gleif",
                "bootstrap.servers": cfg.redpanda.bootstrap_servers,
                "enable.idempotence": "true",
                "acks": "all",
            }
        self.producer = Producer(config)

    @staticmethod
    def delivery_report(err, msg):
        """Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush()."""
        if err is not None:
            logger.error("Message delivery failed: {}".format(err))
            return
        # print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))

    def produce(self, record: dict, topic: str = cfg.redpanda.topic_name):
        try:
            obj = schema.LEICompany(**record)
            self.producer.produce(
                topic=topic,
                value=obj.model_dump_json(),
                key=obj.lei,
                callback=self.delivery_report,
            )
        except Exception as err:
            logger.error(f"Error while producing record {record}, {err=}")
            raise err

    def poll(self, timeout: int):
        self.producer.poll(timeout)

    def flush(self, timeout: int = 10):
        self.producer.flush(timeout)

    def close(self):
        self.producer.poll(10000)
        self.producer.flush()
