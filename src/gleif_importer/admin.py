import logging

from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic
from settings import cfg


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


admin = AdminClient({"bootstrap.servers": cfg.redpanda.bootstrap_servers})

topic = NewTopic(
    topic=cfg.redpanda.topic_name,
    num_partitions=cfg.redpanda.partition_count,
    replication_factor=1,
)


def bootstrap():
    if cfg.redpanda.topic_name in admin.list_topics().topics:
        logger.info(cfg.redpanda.topic_name)
        logger.info(f"Topic {cfg.redpanda.topic_name} already exists.")
    else:
        admin.create_topics([topic])
        logger.error(f"Topic {cfg.redpanda.topic_name} created.")


def delete():
    if cfg.redpanda.topic_name in admin.list_topics().topics:
        admin.delete_topics([cfg.redpanda.topic_name])
        logger.info(f"Topic {cfg.redpanda.topic_name} deleted.")
    else:
        logger.error(f"Topic {cfg.redpanda.topic_name} does not exist.")
