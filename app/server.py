import logging

from admin import bootstrap, delete
from db import Neo4jClient
from flask import Flask, jsonify, request
from flask_cors import CORS
from producer import CompanyProducer
from settings import cfg
from loader import _loader

bootstrap()
app = Flask(__name__)
cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"
neo = Neo4jClient(cfg.neo4j)


gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route("/company", methods=["POST"])
def load_single():
    data = request.json
    producer = CompanyProducer()
    app.logger.debug(f"Processing record: {data}")
    producer.produce(data)
    producer.close()
    return jsonify({"message": "company queued", "data": data}, 200)


@app.route("/load", methods=["GET"])
def load_batch():
    args = request.args
    limit = 0
    if "limit" in args:
        limit = int(args["limit"])

    _loader(app.logger, filepath="/data/gleif.csv", limit=limit)

    return jsonify({"total_companies": neo.stats()})


@app.route("/stats", methods=["GET"])
def stats():
    return jsonify({"total_companies": neo.stats()})


@app.route("/reset", methods=["GET"])
def reset():
    delete()
    bootstrap()
    neo.reset()
    return jsonify({"message": "topic reset"})
