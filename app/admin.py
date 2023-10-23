import logging

from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic
from settings import cfg, Topics


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


admin = AdminClient({"bootstrap.servers": cfg.redpanda.bootstrap_servers})

topic = NewTopic(
    topic=cfg.redpanda.topic_name,
    num_partitions=cfg.redpanda.partition_count,
    replication_factor=1,
)


def bootstrap():
    existing_topics = admin.list_topics().topics

    for topic in Topics:
        if topic not in existing_topics:
            admin.create_topics([NewTopic(topic.value, 3, 1)])
            logger.info(f"Topic {topic.value} created.")
        else:
            logger.info(f"Topic {topic.value} already exists.")


def delete():
    topics = [topic.value for topic in Topics]
    admin.delete_topics(topics)
    logger.info(f"Topic {topics} deleted.")
