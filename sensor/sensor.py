import json
import random
import time
import traceback

import paho.mqtt.client as mqtt

BROKER_HOST = "edge-broker"
BROKER_PORT = 1883
TOPIC = "temperature"

client = mqtt.Client()

while True:
    try:
        client.connect(BROKER_HOST, BROKER_PORT)
        break
    except Exception as e:
        print(traceback.format_exc())
        time.sleep(1)

client.loop_start()

while True:
    temp = random.randint(50, 100)
    payload = {
        "temp": temp
    }
    client.publish(TOPIC, json.dumps(payload))
    print(f"Отправлена температура: {temp}")
    time.sleep(1)
