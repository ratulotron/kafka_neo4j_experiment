FROM docker.redpanda.com/redpandadata/connectors:latest

USER root

RUN yum -y update && \
    yum -y install tar && \
    yum clean all
RUN curl https://client.hub.confluent.io/confluent-hub-client-latest.tar.gz -o /tmp/confluent-hub-client-latest.tar.gz
RUN tar -xzf /tmp/confluent-hub-client-latest.tar.gz -C /tmp
RUN mv /tmp/bin/confluent-hub /usr/local/bin
RUN rm /tmp/confluent-hub-client-latest.tar.gz
RUN confluent-hub install --component-dir /opt/kafka/connect-plugins --no-prompt neo4j/kafka-connect-neo4j:latest
USER redpanda