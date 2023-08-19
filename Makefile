panda:
	docker compose up -d

producer:
	poetry run flask --app app run --debug -p 6000

consumer:
	poetry run python consumer.py
