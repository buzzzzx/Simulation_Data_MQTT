# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/4/6 下午10:48'

"""
发布信息端
"""

import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

# mqtt setting
# MQTT_HOST = "119.23.203.252"
# MQTT_PORT = 61613
MQTT_Broker = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Temperature = "Sensors/Temperature"
MQTT_Topic_Gas = "Sensors/Gas"
MQTT_Topic_Pressure = "Sensors/Pressure"

# test_host = "iot.eclipse.org"
# test_port = 1883


# mqtt functions
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_publish(client, userdata, mid):
    pass


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)


# client.connect(test_host, test_port, Keep_Alive_Interval)
# client.loop_forever()

# =============================
# simulate fake sensor data
# publish to MQTT broker
# =============================

def publish2topic(topic, msg):
    client.publish(topic, msg)
    print("Published: " + str(msg) + " " + "on MQTT Topic: " + str(topic))
    print("")


flag = 0


def publish_fake_data_to_broker():
    threading.Timer(3.0, publish_fake_data_to_broker).start()
    global flag

    if flag == 0:
        """
        publish temperature data
        """
        temperature_data = {}
        temperature_fake_value = float("{0:.2f}".format(random.uniform(1, 20)))
        temperature_data['Sensor_ID'] = "Dummy-1"
        temperature_data['Temperature'] = temperature_fake_value
        temperature_data['Date'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S:%f")
        temperature_json_data = json.dumps(temperature_data)

        print("Publishing fake temperature data: {} 摄氏度 ......".format(str(temperature_fake_value)))
        publish2topic(MQTT_Topic_Temperature, temperature_json_data)

        flag = 1

    elif flag == 1:
        """
        publish gas data
        """
        gas_data = {}
        gas_fake_value = float("{0:.2f}".format(random.uniform(1, 10)))
        gas_data['Sensor_ID'] = "Dummy-2"
        gas_data['Gas'] = gas_fake_value
        gas_data['Date'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S:%f")
        gas_json_data = json.dumps(gas_data)

        print("Publishing fake gas data: {} 立方 ......".format(str(gas_fake_value)))
        publish2topic(MQTT_Topic_Gas, gas_json_data)

        flag = 2

    else:
        """
        publish pressure data
        """
        pressure_data = {}
        pressure_fake_value = float("{0:.2f}".format(random.uniform(1, 10)))
        pressure_data['Sensor_ID'] = "Dummy-3"
        pressure_data['Pressure'] = pressure_fake_value
        pressure_data['Date'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S:%f")
        pressure_json_data = json.dumps(pressure_data)

        print("Publishing fake pressure data: {} KPa ......".format(str(pressure_fake_value)))
        publish2topic(MQTT_Topic_Pressure, pressure_json_data)

        flag = 0


publish_fake_data_to_broker()
