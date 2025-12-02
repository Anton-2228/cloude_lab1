import logging

from flask import Flask

from app.db.db import RedisService
from app.db.redis import RedisStorage
from app.environments import REDIS_HOST, REDIS_PORT


logging.basicConfig(filename="/logs/log.log", filemode="a", level=logging.INFO, force=True)
logger = logging.getLogger(__name__)

app = Flask(__name__)

db = RedisService(RedisStorage(host=REDIS_HOST, port=REDIS_PORT))

@app.route("/")
def index():
    admission_count = db.increment_admission()
    return f"<h1>Admission count:</h1><p>{admission_count}</p>"
