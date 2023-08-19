panda:
	docker compose up -d

producer:
	poetry run flask --app app run --debug -p 6000

consumer:
	poetry run python consumer.py

reload_conn:
	poetry run http DELETE localhost:8083/connectors/Neo4jSinkConnectorJSONString
	poetry run http POST localhost:8083/connectors < ./neo4j-connector.json