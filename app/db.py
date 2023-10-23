import logging
import sys

from neo4j import GraphDatabase
from settings import Neo4jConfig

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

logger = logging.getLogger(__name__)


class Neo4jClient:
    def __init__(self, conf: Neo4jConfig):
        auth = (conf.user, conf.password)
        self.driver = GraphDatabase.driver(conf.uri, auth=auth)

    def close(self):
        self.driver.close()

    def stats(self):
        r = self.driver.session().run("MATCH (n) RETURN count(n) as count").single()
        if r:
            return r["count"]
        return 0

    def create(self, data):
        try:
            with self.driver.session() as session:
                result = session.execute_write(self._create, data)
                logger.info(result)
        except Exception as err:
            logger.error(f"Error creating company: {data=}, {err=}, {type(err)=}")

    @staticmethod
    def _create(tx, data):
        result = tx.run(
            """
            CALL apoc.merge.node(
                ["Company"],
                {lei: $data.lei},
                $data
            )
            YIELD node
            SET node.created_at = coalesce(node.created_at, date())
            SET node.updated_at = date()
            RETURN node

        """,
            data=data,
        )
        return result.single()[0]

    def reset(self):
        query = "MATCH (n) DETACH DELETE n"
        try:
            with self.driver.session() as session:
                result = session.execute_write(lambda tx: tx.run(query))
                logger.info(result)
        except Exception as err:
            logger.error(f"Error resetting database: {err=}, {type(err)=}")
