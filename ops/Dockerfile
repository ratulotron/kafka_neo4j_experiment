FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY ./ops/requirements.txt /src
RUN pip3 install -r requirements.txt

COPY ./src /src

ENTRYPOINT ["/bin/sh", "-c"]
