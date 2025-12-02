import os

os.environ["REDIS_HOST"] = "redis"
os.environ["REDIS_PORT"] = "6380"
os.environ["REDIS_PASSWORD"] = "1234"
os.environ["APP_PORT"] = "5000"
os.environ["LOGGING_DIR"] = "/home/anton/Desktop/облака/lab1/log:/logs"

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
