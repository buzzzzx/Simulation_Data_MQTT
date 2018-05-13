# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/4/7 上午11:55'

"""
Store data to Mysql
influxdb temporarily not available
"""

import pymysql
import json

# mysql config
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'xxxxxxxxx',
    'db': 'Iot_Sensor'
}


# conn = pymysql.connect(**config)
# cur = conn.cursor()
# cur.execute("show databases;")
# print(cur)
#
# cur.close()
# conn.close()


# ================================
# Database Manager Class

class DatabaseManager():
    def __init__(self):
        self.conn = pymysql.connect(**config)
        self.cur = self.conn.cursor()

    def add_record(self, sql_query):
        self.cur.execute(sql_query)
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()


def temp_data_handler(jsonData):
    # parse data
    data_dict = json.loads(jsonData)
    SensorID = data_dict['Sensor_ID']
    Date_and_Time = data_dict['Date']
    Temperature = data_dict['Temperature']

    # store in db table
    db_obj = DatabaseManager()

    sql_query = "insert into Sensor_Temperature_Data (SensorID, Date_n_Time, Temperature) values ('{}', '{}', '{}')".format(
        SensorID, Date_and_Time, str(Temperature))
    db_obj.add_record(sql_query)

    del db_obj

    print("Inserted Temperature Data into Database.")
    print("")


def gas_data_handler(jsonData):
    # parse data
    data_dict = json.loads(jsonData)
    SensorID = data_dict['Sensor_ID']
    Date_and_Time = data_dict['Date']
    Gas = data_dict['Gas']

    # store in db table
    db_obj = DatabaseManager()

    sql_query = "insert into Sensor_Gas_Data (SensorID, Date_n_Time, Gas) values ('{}', '{}', '{}')".format(
        SensorID, Date_and_Time, str(Gas))
    db_obj.add_record(sql_query)

    del db_obj

    print("Inserted Gas Data into Database.")
    print("")


def pressure_data_handler(jsonData):
    # parse data
    data_dict = json.loads(jsonData)
    SensorID = data_dict['Sensor_ID']
    Date_and_Time = data_dict['Date']
    Pressure = data_dict['Pressure']

    # store in db table
    db_obj = DatabaseManager()

    sql_query = "insert into Sensor_Pressure_Data (SensorID, Date_n_Time, Pressure) values ('{}', '{}', '{}')".format(
        SensorID, Date_and_Time, str(Pressure))
    db_obj.add_record(sql_query)

    del db_obj

    print("Inserted Pressure Data into Database.")
    print("")


def sensor_data_handler(topic, jsonData):
    if topic == "Sensors/Temperature":
        temp_data_handler(jsonData)
    elif topic == "Sensors/Gas":
        gas_data_handler(jsonData)
    elif topic == "Sensors/Pressure":
        pressure_data_handler(jsonData)
