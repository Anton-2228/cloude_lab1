import os

REDIS_HOST=os.getenv("REDIS_HOST")
assert REDIS_HOST is not None, "REDIS_HOST not initialized"
REDIS_PORT=os.getenv("REDIS_PORT")
assert REDIS_PORT is not None, "REDIS_PORT not initialized"
REDIS_PASSWORD=os.getenv("REDIS_PASSWORD")
assert REDIS_PASSWORD is not None, "REDIS_PASSWORD not initialized"

APP_PORT=os.getenv("APP_PORT")
assert APP_PORT is not None, "APP_PORT not initialized"

LOGGING_DIR=os.getenv("LOGGING_DIR")
assert LOGGING_DIR is not None, "LOGGING_DIR not initialized"
