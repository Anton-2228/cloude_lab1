import json
import random
import time

import paho.mqtt.client as mqtt

BROKER_HOST = "temperature-broker"
BROKER_PORT = 1883
TOPIC = "temperature"

client = mqtt.Client()

client.connect(BROKER_HOST, BROKER_PORT)

client.loop_start()

while True:
    temp = random.randint(50, 100)
    payload = {
        "temp": temp
    }
    client.publish(TOPIC, json.dumps(payload))
    print(f"Отправлена температура: {temp}")
    time.sleep(1)
