DOCKER_COMPOSE_CMD=docker compose -f ./ops/docker-compose.yml

req:
	poetry export -f requirements.txt --output ./ops/requirements.txt --without-hashes

build:
	docker build -t gleif_importer:latest -f ./ops/Dockerfile .
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

export_schema:
	poetry run datamodel-codegen \
		--output app/gleif_importer/schema_v2.py --output-model-type pydantic_v2.BaseModel \
		--input data/gleif.csv --input-file-type csv \
		--original-field-name-delimiter . --snake-case-field \
		--use-double-quotes \
		--field-constraints \
		--disable-timestamp --use-standard-collections \
 		--use-union-operator --use-schema-description --use-field-description --reuse-model \
 		--target-python-version 3.11 \
 		--wrap-string-literal \
 		--capitalise-enum-members \
 		--class-name LEICompany

 		# --strict-types str bytes int float bool \
