import csv
import json
import logging
from typing import Any

import orjson
from flask import Flask, jsonify, request
from flask_cors import CORS
# from kafka import KafkaProducer, KafkaAdminClient
# from kafka.admin import NewTopic
from pydantic import BaseModel, Field, model_validator
from smart_open import open
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic
from db import Neo4jClient


BOOTSTRAP_SERVERS = "localhost:19092"
TOPIC_NAME = "companies"
PARTITION_COUNT = 3

admin = AdminClient({"bootstrap.servers": BOOTSTRAP_SERVERS})
topic = NewTopic(
                topic=TOPIC_NAME,
                num_partitions=PARTITION_COUNT,
                replication_factor=1,
            )


if TOPIC_NAME in admin.list_topics().topics:
    print(TOPIC_NAME)
    print(f"Topic {TOPIC_NAME} already exists.")
else:
    admin.create_topics([topic])
    print(f"Topic {TOPIC_NAME} created.")


class Schema(BaseModel):
    lei: str = Field(alias="LEI")
    legal_name: str = Field(alias="Entity.LegalName")
    address_line_1: str | None = Field(None, alias="Entity.LegalAddress.FirstAddressLine")
    address_line_2: str | None = Field(None, alias="Entity.LegalAddress.AdditionalAddressLine.1")
    city: str | None = Field(None, alias="Entity.LegalAddress.City")
    country: str | None = Field(None, alias="Entity.LegalAddress.Country")
    postal_code: str | None = Field(None, alias="Entity.LegalAddress.PostalCode")

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True
        json_loads = orjson.loads
        json_dumps = orjson.dumps

    @model_validator(mode='before')
    @classmethod
    def check_empty_string(cls, data: Any) -> Any:
        for key, value in data.items():
            if value == "":
                data[key] = None
        return data


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
logger = logging.getLogger(__name__)


def delivery_callback(err, msg):
    if err:
        print("ERROR: Message failed delivery: {}".format(err))
    else:
        print(
            "Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(),
                key=msg.key().decode("utf-8"),
                value=msg.value().decode("utf-8"),
            )
        )


@app.route("/load", methods=["GET"])
def load():
    limit = int(request.args.get("limit", "0"))

    try:
        producer = Producer(
            {
                "transactional.id": "gleif",
                "enable.idempotence": True,
                "bootstrap.servers": BOOTSTRAP_SERVERS,
            }
        )
        with open("./data/gleif.csv") as dataset:
            csv_reader = csv.DictReader(dataset, delimiter=",")

            for current_num, record in enumerate(csv_reader, start=1):
                try:
                    app.logger.info(f"Processing record no. {current_num}")
                    obj = Schema(**record)
                    producer.produce(TOPIC_NAME, obj.model_dump_json(), callback=delivery_callback)
                except Exception as e:
                    app.logger.error(f"Error processing record no. {current_num}:", exc_info=True,)
                    continue
                if (current_num != 0) and (current_num == limit):
                    break
            producer.poll(10000)
            producer.flush()
        return jsonify({"total_companies": current_num})
    except Exception as err:
        msg = f"Unexpected {err=}, {type(err)=}"
        print(msg)
        return jsonify({"error": msg})


@app.route("/stats", methods=["GET"])
def stats():
    neo = Neo4jClient("bolt://localhost:7687", "neo4j", "password")
    return jsonify({"total_companies": neo.stats()})
