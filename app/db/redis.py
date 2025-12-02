import pickle
from typing import Any, Optional, Type, TypeVar

from redis import Redis

from app.environments import REDIS_PASSWORD

T = TypeVar("T")

class RedisStorage:
    def __init__(self, host: str, port: int):
        self.redis = Redis(host=host, port=int(port), db=0, password=REDIS_PASSWORD)

    def _get(self, key: str, return_type: Type[T]) -> Optional[T]:
        raw_data: Optional[bytes] = self.redis.get(key)
        if raw_data is None:
            return None
        data = pickle.loads(raw_data)
        assert isinstance(data, return_type)
        return data

    def get_str(self, key: str) -> Optional[str]:
        return self._get(key=key, return_type=str)

    def get_dict(self, key: str) -> Optional[dict]:
        return self._get(key=key, return_type=dict)

    def get_list(self, key: str) -> Optional[list]:
        return self._get(key=key, return_type=list)

    def get_value(self, key: str, return_type: Type[T]) -> Optional[T]:
        return self._get(key=key, return_type=return_type)

    def set_value(self, key: str, value: Any) -> None:
        self.redis.set(name=key, value=pickle.dumps(value))

    def delete_value(self, key: str) -> None:
        self.redis.delete(key)
