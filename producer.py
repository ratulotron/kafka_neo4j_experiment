import csv
import logging
from typing import Any
from smart_open import open
from pydantic import BaseModel, Field, model_validator
from kafka import KafkaProducer
import json


logger = logging.getLogger(__name__)

