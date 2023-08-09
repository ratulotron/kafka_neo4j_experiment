from neo4j import GraphDatabase


class Neo4jClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def stats(self):
        return self.driver.session().run("MATCH (n) RETURN count(n) as count").single()[0]

    def create(self, data):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create, data)
            print(greeting)

    @staticmethod
    def _create(tx, data):
        result = tx.run("""
            CALL apoc.merge.node(
                ["Company"],
                {lei: $data.lei},
                $data.company
            )
            YIELD node
            SET node.created_at = coalesce(node.created_at, date())
            SET node.updated_at = date()
            RETURN node

        """, data=data)
        return result.single()[0]
