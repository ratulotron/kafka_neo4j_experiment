from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic

from settings import cfg


admin = AdminClient({"bootstrap.servers": cfg.redpanda.bootstrap_servers})

topic = NewTopic(
    topic=cfg.redpanda.topic_name,
    num_partitions=cfg.redpanda.partition_count,
    replication_factor=1,
)


def bootstrap():
    if cfg.redpanda.topic_name in admin.list_topics().topics:
        print(cfg.redpanda.topic_name)
        print(f"Topic {cfg.redpanda.topic_name} already exists.")
    else:
        admin.create_topics([topic])
        print(f"Topic {cfg.redpanda.topic_name} created.")


def delete():
    if cfg.redpanda.topic_name in admin.list_topics().topics:
        admin.delete_topics([cfg.redpanda.topic_name])
        print(f"Topic {cfg.redpanda.topic_name} deleted.")
    else:
        print(f"Topic {cfg.redpanda.topic_name} does not exist.")
