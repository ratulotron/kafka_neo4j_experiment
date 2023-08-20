DOCKER_COMPOSE_CMD=docker compose -f ./ops/docker-compose.yml

req:
	poetry export -f requirements.txt --output ./ops/requirements.txt --without-hashes

build:
	docker build -t gleif_importer:latest -f ./ops/base.Dockerfile .
	${DOCKER_COMPOSE_CMD} build

up:
	${DOCKER_COMPOSE_CMD} up

consumers:
	${DOCKER_COMPOSE_CMD} --profile consumer up consumer

down:
	${DOCKER_COMPOSE_CMD} down

all: req build up


reload_conn:
	poetry run http DELETE localhost:8083/connectors/Neo4jSinkConnectorJSONString
	poetry run http POST localhost:8083/connectors < ./neo4j-connector.json

benchmark:
	poetry run python loader.py --limit 10000 --benchmark 1
