FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./ops/requirements.txt /app
RUN pip3 install -r requirements.txt

COPY ./src/gleif_importer /app

ENTRYPOINT ["/bin/sh", "-c"]
