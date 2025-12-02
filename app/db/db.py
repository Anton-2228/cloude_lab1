import logging
from typing import List, Optional

from app.db.redis import RedisStorage

logger = logging.getLogger(__name__)


class RedisService:
    def __init__(self, redis_client: RedisStorage):
        self.redis_client = redis_client

    def increment_admission(self) -> int:
        count_admissions = self.redis_client.get_value(key="count_admissions", return_type=int)
        count_admissions += 1
        self.redis_client.set_value(key="count_admissions", value=count_admissions)
        return count_admissions

    def get_count_admissions(self) -> int:
        count_admissions = self.redis_client.get_value(key="count_admissions", return_type=int)
        return count_admissions
