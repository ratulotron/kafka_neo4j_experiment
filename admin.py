from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic

from configs import BOOTSTRAP_SERVERS, TOPIC_NAME, PARTITION_COUNT

admin = AdminClient({"bootstrap.servers": BOOTSTRAP_SERVERS})

topic = NewTopic(
    topic=TOPIC_NAME,
    num_partitions=PARTITION_COUNT,
    replication_factor=1,
)


def bootstrap():
    if TOPIC_NAME in admin.list_topics().topics:
        print(TOPIC_NAME)
        print(f"Topic {TOPIC_NAME} already exists.")
    else:
        admin.create_topics([topic])
        print(f"Topic {TOPIC_NAME} created.")


def delete():
    if TOPIC_NAME in admin.list_topics().topics:
        admin.delete_topics([TOPIC_NAME])
        print(f"Topic {TOPIC_NAME} deleted.")
    else:
        print(f"Topic {TOPIC_NAME} does not exist.")


def purge():
    if TOPIC_NAME in admin.list_topics().topics:
        print(f"Topic {TOPIC_NAME} deleted.")
    else:
        print(f"Topic {TOPIC_NAME} does not exist.")