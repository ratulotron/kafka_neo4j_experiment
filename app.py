import csv
import json
import logging
from typing import Any
from flask import Flask, jsonify, request
from flask_cors import CORS
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from pydantic import BaseModel, Field, model_validator
from smart_open import open

from db import Neo4jClient


class Admin:
    def __init__(self, brokers):
        self.admin = KafkaAdminClient(bootstrap_servers=brokers)

    def topic_exists(self, topic_name):
        topics_metadata = self.admin.list_topics()
        return topic_name in topics_metadata

    def create_topic(self, topic_name, num_partitions=1, replication_factor=1):
        if not self.topic_exists(topic_name):
            new_topic = NewTopic(
                name=topic_name,
                num_partitions=num_partitions,
                replication_factor=replication_factor,
            )
            self.admin.create_topics([new_topic])
            print(f"Topic {topic_name} created.")
        else:
            print(f"Topic {topic_name} already exists.")

    def close(self):
        self.admin.close()


class Producer:
    def __init__(self, brokers, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            transactional_id="gleif",
            enable_idempotence=True,
            bootstrap_servers=brokers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def add_company(self, lei: str, company: dict[str, Any]):
        self.producer.send(
            self.topic,
            {"lei": lei, "company": company},
            lei.encode("utf-8"),
        )
        self.producer.flush()

    def close(self):
        self.producer.close()


class Schema(BaseModel):
    lei: str = Field(alias="LEI")
    legal_name: str = Field(alias="Entity.LegalName")
    address_line_1: str | None = Field(None, alias="Entity.LegalAddress.FirstAddressLine")
    address_line_2: str | None = Field(None, alias="Entity.LegalAddress.AdditionalAddressLine.1")
    city: str | None = Field(None, alias="Entity.LegalAddress.City")
    country: str | None = Field(None, alias="Entity.LegalAddress.Country")
    postal_code: str | None = Field(None, alias="Entity.LegalAddress.PostalCode")

    @model_validator(mode='before')
    @classmethod
    def check_empty_string(cls, data: Any) -> Any:
        for key, value in data.items():
            if value == "":
                data[key] = None
        return data


BOOTSTRAP_SERVERS = ["localhost:19092"]
TOPIC_NAME = "companies"

admin = Admin(BOOTSTRAP_SERVERS)
admin.create_topic(TOPIC_NAME, num_partitions=3, replication_factor=1)

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
logger = logging.getLogger(__name__)


@app.route("/load", methods=["GET"])
def load():
    limit = int(request.args.get("limit", "0"))

    try:
        producer = Producer(BOOTSTRAP_SERVERS, TOPIC_NAME)
        with open("./data/gleif.csv") as dataset:
            csv_reader = csv.DictReader(dataset, delimiter=",")

            for current_num, record in enumerate(csv_reader, start=1):
                try:
                    app.logger.info(f"Processing record no. {current_num}")
                    obj = Schema(**record)
                    producer.add_company(obj.lei, obj.model_dump())
                except Exception as e:
                    app.logger.error(f"Error processing record no. {current_num}:", exc_info=True,)
                    continue
                if (current_num != 0) and (current_num == limit):
                    break
        producer.close()
        return jsonify({"total_companies": current_num})
    except Exception as err:
        msg = f"Unexpected {err=}, {type(err)=}"
        print(msg)
        return jsonify({"error": msg})


@app.route("/stats", methods=["GET"])
def stats():
    neo = Neo4jClient("bolt://localhost:7687", "neo4j", "password")
    return jsonify({"total_companies": neo.stats()})
