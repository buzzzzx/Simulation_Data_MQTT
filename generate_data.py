# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/5/28 下午10:23'

"""
生成一个家庭一年（365 天）每天的水电气用量
"""

import random, pymysql, datetime


def generate_spring(month):
    season = "Spring"
    if month == 3:
        days = 31
        water_min = 0.26
        water_max = 0.39
        elec_min = 1.49
        elec_max = 1.69
        gas_min = 0.84
        gas_max = 0.99
    elif month == 4:
        days = 30
        water_min = 0.27
        water_max = 0.43
        elec_min = 1.33
        elec_max = 1.50
        gas_min = 0.80
        gas_max = 0.92
    else:
        days = 31
        water_min = 0.31
        water_max = 0.48
        elec_min = 1.40
        elec_max = 1.61
        gas_min = 0.77
        gas_max = 0.90

    for i in range(1, days + 1):
        ddate = datetime.date(year, month, i).strftime("%Y-%m-%d")
        water = round(random.uniform(water_min, water_max), 3)
        elec = round(random.uniform(elec_min, elec_max), 3)
        gas = round(random.uniform(gas_min, gas_max), 3)
        sql_query = "insert into DataConsumption (ddate, waterconsumption, elecconsumption, gasconsumption, season) values ('{}', '{}', '{}', '{}', '{}')".format(
            ddate, water, elec, gas, season)
        cur.execute(sql_query)
        conn.commit()


def generate_summer(month):
    season = "Summer"
    if month == 6:
        days = 30
        water_min = 0.41
        water_max = 0.62
        elec_min = 1.71
        elec_max = 1.90
        gas_min = 0.60
        gas_max = 0.80
    elif month == 7:
        days = 31
        water_min = 0.50
        water_max = 0.72
        elec_min = 1.78
        elec_max = 2.00
        gas_min = 0.55
        gas_max = 0.70
    else:
        days = 31
        water_min = 0.45
        water_max = 0.62
        elec_min = 1.79
        elec_max = 1.99
        gas_min = 0.49
        gas_max = 0.68

    for i in range(1, days + 1):
        ddate = datetime.date(year, month, i).strftime("%Y-%m-%d")
        water = round(random.uniform(water_min, water_max), 3)
        elec = round(random.uniform(elec_min, elec_max), 3)
        gas = round(random.uniform(gas_min, gas_max), 3)
        sql_query = "insert into DataConsumption (ddate, waterconsumption, elecconsumption, gasconsumption, season) values ('{}', '{}', '{}', '{}', '{}')".format(
            ddate, water, elec, gas, season)
        cur.execute(sql_query)
        conn.commit()


def generate_fall(month):
    season = "Fall"
    if month == 9:
        days = 30
        water_min = 0.29
        water_max = 0.50
        elec_min = 1.58
        elec_max = 1.77
        gas_min = 0.57
        gas_max = 0.80
    elif month == 10:
        days = 31
        water_min = 0.27
        water_max = 0.39
        elec_min = 1.63
        elec_max = 1.80
        gas_min = 0.83
        gas_max = 0.90
    else:
        days = 30
        water_min = 0.27
        water_max = 0.40
        elec_min = 1.68
        elec_max = 1.80
        gas_min = 0.86
        gas_max = 0.99

    for i in range(1, days + 1):
        ddate = datetime.date(year, month, i).strftime("%Y-%m-%d")
        water = round(random.uniform(water_min, water_max), 3)
        elec = round(random.uniform(elec_min, elec_max), 3)
        gas = round(random.uniform(gas_min, gas_max), 3)
        sql_query = "insert into DataConsumption (ddate, waterconsumption, elecconsumption, gasconsumption, season) values ('{}', '{}', '{}', '{}', '{}')".format(
            ddate, water, elec, gas, season)
        cur.execute(sql_query)
        conn.commit()


def generate_winter(month):
    season = "Winter"
    if month == 12:
        days = 31
        water_min = 0.29
        water_max = 0.44
        elec_min = 1.72
        elec_max = 1.84
        gas_min = 0.90
        gas_max = 1.03
    elif month == 1:
        days = 31
        water_min = 0.28
        water_max = 0.43
        elec_min = 1.71
        elec_max = 1.88
        gas_min = 0.97
        gas_max = 1.13
    else:
        days = 28
        water_min = 0.28
        water_max = 0.44
        elec_min = 1.68
        elec_max = 1.84
        gas_min = 0.91
        gas_max = 1.07

    for i in range(1, days + 1):
        ddate = datetime.date(year, month, i).strftime("%Y-%m-%d")
        water = round(random.uniform(water_min, water_max), 3)
        elec = round(random.uniform(elec_min, elec_max), 3)
        gas = round(random.uniform(gas_min, gas_max), 3)
        sql_query = "insert into DataConsumption (ddate, waterconsumption, elecconsumption, gasconsumption, season) values ('{}', '{}', '{}', '{}', '{}')".format(
            ddate, water, elec, gas, season)
        cur.execute(sql_query)
        conn.commit()


if __name__ == '__main__':

    # connect mysql
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'batman123',
        'db': 'FamilyData'
    }
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    year = 2017

    generate_winter(1)
    generate_winter(2)

    for month in range(3, 6):
        generate_spring(month)

    for month in range(6, 9):
        generate_summer(month)

    for month in range(9, 12):
        generate_fall(month)

    generate_winter(12)

    cur.close()
    conn.close()
