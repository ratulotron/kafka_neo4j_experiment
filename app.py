import csv
import time
from datetime import timedelta

from flask import Flask, jsonify, request
from flask_cors import CORS
from smart_open import open


from admin import bootstrap, delete
from db import Neo4jClient
from producer import CompanyProducer


bootstrap()
app = Flask(__name__)
cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"
neo = Neo4jClient("bolt://localhost:7687", "neo4j", "password")


@app.route("/load", methods=["GET"])
def load():
    limit = int(request.args.get("limit", "0"))

    try:
        dataset = open("./data/gleif.csv")
        csv_reader = csv.DictReader(dataset, delimiter=",")
    except Exception as err:
        msg = f"Unexpected {err=}, {type(err)=}"
        print(msg)
        return jsonify({"error": msg})

    producer = CompanyProducer()
    current_num = 0
    start_time = time.monotonic()
    for current_num, record in enumerate(csv_reader, start=1):
        app.logger.info(f"Processing record no. {current_num}")
        producer.produce(record)
        producer.poll(0)
        if (current_num != 0) and (current_num == limit):
            break
    producer.close()
    end_time = time.monotonic()
    dataset.close()
    app.logger.info(f"Total companies: {current_num}")
    app.logger.info(f"Total time: {timedelta(seconds=(end_time - start_time))}")
    return jsonify({"total_companies": current_num})


@app.route("/stats", methods=["GET"])
def stats():
    return jsonify({"total_companies": neo.stats()})


@app.route("/reset", methods=["GET"])
def reset():
    delete()
    bootstrap()
    neo.reset()
    return jsonify({"message": "topic reset"})
