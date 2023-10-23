from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum


class Topics(Enum):
    RECORD = "record"
    COMPANY = "company"
    RELATIONSHIP = "relationship"


class Neo4jConfig(BaseModel):
    uri: str = "bolt://localhost:7687"
    user: str = "neo4j"
    password: str = "password"


class RedpandaConfig(BaseModel):
    bootstrap_servers: str = "localhost:19092"
    topic_name: str = "companies"
    partition_count: int = 3


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    neo4j: Neo4jConfig = Neo4jConfig()
    redpanda: RedpandaConfig = RedpandaConfig()


cfg = Config()
