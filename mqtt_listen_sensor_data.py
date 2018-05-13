# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/4/7 上午11:48'

"""
订阅并接收消息端
"""

import paho.mqtt.client as mqtt
from store_data_to_db import sensor_data_handler


# mqtt setting
MQTT_Broker = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Sensors/#"

test_host = "iot.eclipse.org"
test_port = 1883


def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_Topic, 0)


def on_message(client, userdata, msg):
    print("MQTT Data Received......")
    print("MQTT Topic: " + msg.topic)
    print("Data: " + str(msg.payload))

    sensor_data_handler(msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass


client = mqtt.Client()

# callback functions
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
client.loop_forever()
