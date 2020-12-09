from typing import List, Optional
import session_factory
from weather_model import WeatherPoint
import requests
from datetime import datetime
from time import sleep

#import json, pprint


def record_gov_point(point: WeatherPoint):
    session = session_factory.create_session()

    session.add(point)
    session.commit()
    session.close()

def get_gov_point(new_data: dict):
    point = WeatherPoint()

    point.station = new_data["station"]
    point.temperature = new_data["temperature"]["value"]
    time_format = "%Y-%m-%dT%H:%M:%S%z"
    point.timestamp = datetime.strptime(new_data["timestamp"], time_format)    # (DateTime)
    point.rawMessage = new_data["rawMessage"]
    point.textDescription = new_data["textDescription"]
    point.icon = new_data["icon"]
    point.presentWeather = ",".join(new_data["presentWeather"])
    point.temperature = new_data["temperature"]["value"]    # (Float)
    point.temperature_unit = new_data["temperature"]["unitCode"]    # (String)
    point.dewpoint = new_data["dewpoint"]["value"]    # (Float)
    point.dewpoint_unit = new_data["dewpoint"]["unitCode"]    # (String)
    point.windDirection = new_data["windDirection"]["value"]    # (Float)
    point.windDirection_unit = new_data["windDirection"]["unitCode"]    # (String)
    point.windSpeed = new_data["windSpeed"]["value"]    # (Float)
    point.windSpeed_unit = new_data["windSpeed"]["unitCode"]    # (String)
    point.windGust = new_data["windGust"]["value"]    # (Float)
    point.windGust_unit = new_data["windGust"]["unitCode"]    # (String)
    point.barometricPressure = new_data["barometricPressure"]["value"]    # (Float)
    point.barometricPressure_unit = new_data["barometricPressure"]["unitCode"]    # (String)
    point.seaLevelPressure = new_data["seaLevelPressure"]["value"]    # (Float)
    point.seaLevelPressure_unit = new_data["seaLevelPressure"]["unitCode"]    # (String)
    point.visibility = new_data["visibility"]["value"]    # (Float)
    point.visibility_unit = new_data["visibility"]["unitCode"]    # (String)
    point.maxTemperatureLast24Hours = new_data["maxTemperatureLast24Hours"]["value"]    # (Float)
    point.maxTemperatureLast24Hours_unit = new_data["maxTemperatureLast24Hours"]["unitCode"]    # (String)
    point.minTemperatureLast24Hours = new_data["minTemperatureLast24Hours"]["value"]    # (Float)
    point.minTemperatureLast24Hours_unit = new_data["minTemperatureLast24Hours"]["unitCode"]    # (String)
    point.precipitationLastHour = new_data["precipitationLastHour"]["value"]    # (Float)
    point.precipitationLastHour_unit = new_data["precipitationLastHour"]["unitCode"]    # (String)
    point.precipitationLast3Hours = new_data["precipitationLast3Hours"]["value"]    # (Float)
    point.precipitationLast3Hours_unit = new_data["precipitationLast3Hours"]["unitCode"]    # (String)
    point.precipitationLast6Hours = new_data["precipitationLast6Hours"]["value"]    # (Float)
    point.precipitationLast6Hours_unit = new_data["precipitationLast6Hours"]["unitCode"]    # (String)
    point.relativeHumidity = new_data["relativeHumidity"]["value"]    # (Float)
    point.relativeHumidity_unit = new_data["relativeHumidity"]["unitCode"]    # (String)
    point.windChill = new_data["windChill"]["value"]    # (Float)
    point.windChill_unit = new_data["windChill"]["unitCode"]    # (String)
    point.heatIndex = new_data["heatIndex"]["value"]    # (Float)
    point.heatIndex_unit = new_data["heatIndex"]["unitCode"]    # (String)
    point.cloudLayers = new_data["cloudLayers"][0]["base"]["value"]    # (Float)
    point.cloudLayers_unit = new_data["cloudLayers"][0]["base"]["unitCode"]    # (String)
    point.cloudLayers_amount = new_data["cloudLayers"][0]["amount"] # String
    return point


def get_gov_api():
    req = requests.get("https://api.weather.gov/stations/KCNK/observations/latest")
    return req.json()

def main():
    # with open("weather.json", "r") as json_file:
    #     current_json = json_file.read()
    # current_data = json.loads(current_json)
    while True:
        current_data = get_gov_api()
        new_data_point = get_gov_point(current_data["properties"])
        record_gov_point(new_data_point)
        sleep(60*10)

if __name__ == "__main__":
    main()