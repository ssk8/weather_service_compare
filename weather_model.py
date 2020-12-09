from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

ModelBase = declarative_base()


class WeatherPoint(ModelBase):
    __tablename__ = 'conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.now)
    station = Column(String)
    timestamp = Column(DateTime)
    rawMessage = Column(String)
    textDescription = Column(String)
    icon = Column(String)
    presentWeather = Column(String)
    temperature = Column(Float)
    temperature_unit = Column(String)
    dewpoint = Column(Float)
    dewpoint_unit = Column(String)
    windDirection = Column(Float)
    windDirection_unit = Column(String)
    windSpeed = Column(Float)
    windSpeed_unit = Column(String)
    windGust = Column(Float)
    windGust_unit = Column(String)
    barometricPressure = Column(Integer)
    barometricPressure_unit = Column(String)
    seaLevelPressure = Column(Integer)
    seaLevelPressure_unit = Column(String)
    visibility = Column(Integer)
    visibility_unit = Column(String)
    maxTemperatureLast24Hours = Column(Float)
    maxTemperatureLast24Hours_unit = Column(String)
    minTemperatureLast24Hours = Column(Float)
    minTemperatureLast24Hours_unit = Column(String)
    precipitationLastHour = Column(Float)
    precipitationLastHour_unit = Column(String)
    precipitationLast3Hours = Column(Float)
    precipitationLast3Hours_unit = Column(String)
    precipitationLast6Hours = Column(Float)
    precipitationLast6Hours_unit = Column(String)
    relativeHumidity = Column(Float)
    relativeHumidity_unit = Column(String)
    windChill = Column(Float)
    windChill_unit = Column(String)
    heatIndex = Column(Float)
    heatIndex_unit = Column(String)
    cloudLayers = Column(Float)
    cloudLayers_unit = Column(String)
    cloudLayers_amount = Column(String)

