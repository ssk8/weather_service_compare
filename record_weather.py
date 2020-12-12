import session_factory
from weather_model import WeatherPoint
import requests
from datetime import datetime, timedelta
from time import sleep
from os import environ

import json, pprint


def record_point(point: WeatherPoint):
    session = session_factory.create_session()
    session.add(point)
    session.commit()
    session.close()

def get_gov_point(new_data: dict):
    point = WeatherPoint()

    point.station = new_data["station"]
    time_format = "%Y-%m-%dT%H:%M:%S%z"
    point.timestamp = datetime.strptime(new_data["timestamp"], time_format)    # (DateTime)
    point.rawMessage = new_data["rawMessage"]
    point.textDescription = new_data["textDescription"]
    point.icon = new_data["icon"]
    if new_data["presentWeather"]:
        point.presentWeather = ", ".join([w["weather"] for w in new_data["presentWeather"]])
    point.temperature = new_data["temperature"]["value"]    # (Float)
    point.temperature_unit = new_data["temperature"]["unitCode"][5:]    # (String)
    point.dewpoint = new_data["dewpoint"]["value"]    # (Float)
    point.dewpoint_unit = new_data["dewpoint"]["unitCode"][5:]   # (String)
    point.windDirection = new_data["windDirection"]["value"]    # (Float)
    point.windDirection_unit = new_data["windDirection"]["unitCode"][5:]   # (String)
    point.windSpeed = new_data["windSpeed"]["value"]    # (Float)
    point.windSpeed_unit = new_data["windSpeed"]["unitCode"][5:]   # (String)
    point.windGust = new_data["windGust"]["value"]    # (Float)
    point.windGust_unit = new_data["windGust"]["unitCode"][5:]   # (String)
    point.barometricPressure = new_data["barometricPressure"]["value"]    # (Float)
    point.barometricPressure_unit = new_data["barometricPressure"]["unitCode"][5:]   # (String)
    point.seaLevelPressure = new_data["seaLevelPressure"]["value"]    # (Float)
    point.seaLevelPressure_unit = new_data["seaLevelPressure"]["unitCode"][5:]   # (String)
    point.visibility = new_data["visibility"]["value"]    # (Float)
    point.visibility_unit = new_data["visibility"]["unitCode"][5:]   # (String)
    point.maxTemperatureLast24Hours = new_data["maxTemperatureLast24Hours"]["value"]    # (Float)
    point.maxTemperatureLast24Hours_unit = new_data["maxTemperatureLast24Hours"]["unitCode"][5:]   # (String)
    point.minTemperatureLast24Hours = new_data["minTemperatureLast24Hours"]["value"]    # (Float)
    point.minTemperatureLast24Hours_unit = new_data["minTemperatureLast24Hours"]["unitCode"][5:]   # (String)
    point.precipitationLastHour = new_data["precipitationLastHour"]["value"]    # (Float)
    point.precipitationLastHour_unit = new_data["precipitationLastHour"]["unitCode"][5:]   # (String)
    point.precipitationLast3Hours = new_data["precipitationLast3Hours"]["value"]    # (Float)
    point.precipitationLast3Hours_unit = new_data["precipitationLast3Hours"]["unitCode"][5:]   # (String)
    point.precipitationLast6Hours = new_data["precipitationLast6Hours"]["value"]    # (Float)
    point.precipitationLast6Hours_unit = new_data["precipitationLast6Hours"]["unitCode"][5:]   # (String)
    point.relativeHumidity = new_data["relativeHumidity"]["value"]    # (Float)
    point.relativeHumidity_unit = new_data["relativeHumidity"]["unitCode"][5:]   # (String)
    point.windChill = new_data["windChill"]["value"]    # (Float)
    point.windChill_unit = new_data["windChill"]["unitCode"][5:]   # (String)
    point.heatIndex = new_data["heatIndex"]["value"]    # (Float)
    point.heatIndex_unit = new_data["heatIndex"]["unitCode"][5:]   # (String)
    point.cloudLayers = new_data["cloudLayers"][0]["base"]["value"]    # (Float)
    point.cloudLayers_unit = new_data["cloudLayers"][0]["base"]["unitCode"][5:]   # (String)
    point.cloudLayers_amount = new_data["cloudLayers"][0]["amount"] # String
    return point


def get_openweather_point(new_data: dict):
    point = WeatherPoint()
    point.station = f'openweather: {new_data["name"]}'
    point.timestamp = datetime.fromtimestamp(new_data["dt"])    # (DateTime)
    point.textDescription = new_data["weather"][0]["main"]
    point.icon = new_data["weather"][0]["icon"]
    point.presentWeather = new_data["weather"][0]["description"]
    point.temperature = new_data["main"]["temp"]
    point.temperature_unit = "degK"
    point.windDirection = new_data["wind"]["deg"]    # (Float)
    point.windDirection_unit = "deg"
    point.windSpeed = new_data["wind"]["speed"]    # (Float)
    point.windSpeed_unit = "kph or mps???"
    point.barometricPressure = new_data["main"]["pressure"]    # (Float)
    point.barometricPressure_unit = "saa?"
    point.visibility = new_data["visibility"]
    point.visibility_unit = "m"
    point.maxTemperatureLast24Hours = new_data["main"]["temp_max"]    # (Float)
    point.maxTemperatureLast24Hours_unit = "degK"
    point.minTemperatureLast24Hours = new_data["main"]["temp_min"]    # (Float)
    point.minTemperatureLast24Hours_unit = "degK"
    point.relativeHumidity = new_data["main"]["humidity"]    # (Float)
    point.relativeHumidity_unit = "percent"
    point.heatIndex = new_data["main"]["feels_like"]    # (Float)
    point.heatIndex_unit = "degK"
    point.cloudLayers = new_data["clouds"]["all"]    # (Float)
    return point


def get_gov_api():
    req = requests.get("https://api.weather.gov/stations/KCNK/observations/latest")
    return req.json()

def rec_gov_to_db():
    # with open("data/gov/latest3.json", "r") as json_file:
    #     current_json = json_file.read()
    # current_data = json.loads(current_json)
    # pprint.pp(current_data)
    current_data = get_gov_api()
    new_data_point = get_gov_point(current_data["properties"])
    record_point(new_data_point)


def get_openweather_api():
    LAT, LON = "39.571", "-97.662"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": environ['OPEN_WEATHER_TOKEN'], "lat": LAT, "lon": LON, }
    response = requests.get(url=url, params=params)
    return response.json()


def rec_openweather_to_db():
    # with open("data/openweather/weather.json", "r") as json_file:
    #     current_json = json_file.read()
    # current_data = json.loads(current_json)
    # pprint.pp(current_data)
    current_data = get_openweather_api()
    new_data_point = get_openweather_point(current_data)
    record_point(new_data_point)

def main():
    last_update = datetime.now()-timedelta(minutes=20)

    while True:
        now = datetime.now()       
        if (now-last_update).seconds/60 > 15:
            rec_gov_to_db()
            rec_openweather_to_db()
            last_update = datetime.now()
            print(f"updated at {last_update}")
        sleep(60)

if __name__ == "__main__":
    main()
