import os
import time
import traceback

import paho.mqtt.client as mqtt

BROKER_HOST = "cloud-broker"
BROKER_PORT = 1883
TOPIC = "alerts"

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Получена температура: {msg.payload.decode('utf-8')}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

while True:
    try:
        client.connect(BROKER_HOST, BROKER_PORT, 60)
        break
    except Exception as e:
        print(traceback.format_exc())
        time.sleep(1)

client.loop_forever()
