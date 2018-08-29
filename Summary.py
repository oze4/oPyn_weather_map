from CityCoordinate import CityCoordinate as City_Coordinate_Info
from Clouds import Clouds as Clouds_Info
from DescriptionInfo import DescriptionInfo as Description__Info
from Measurements import Measurements as Measurements_Info
from Sys import Sys as Sys_Info
from Wind import Wind as Wind_Info


class Summary(object):
    Timestamp = str()
    Weather_Id = str()
    City = str()
    Code = str()
    Visibility = str()
    Base_ = str()
    Date_Time = str()
    Wind = Wind_Info()
    Sys = Sys_Info()
    Measurements = Measurements_Info()
    DescriptionInfo = Description__Info()
    Clouds = Clouds_Info()
    Coordinates = City_Coordinate_Info()

    def __init__(self, timestamp, weather_id, city, code, visibility, base_, date_time,
                 wind,
                 sys,
                 measurements,
                 description_info,
                 clouds,
                 city_coordinate
                 ):
        self.Timestamp = timestamp
        self.Weather_Id = weather_id
        self.City = city
        self.Code = code
        self.Visibility = visibility
        self.Base_ = base_
        self.Date_Time = date_time
        self.Wind.Speed = wind.Speed
        self.Sys.Country = sys.Country
        self.Sys.Id = sys.Id
        self.Measurements.Humidity = measurements.Humidity
        self.Measurements.Pressure = measurements.Pressure
        self.Measurements.Temp = measurements.Temp
        self.Measurements.Temp_Max = measurements.Temp_Max
        self.Measurements.Temp_Min = measurements.Temp_Min
        self.DescriptionInfo.Id = description_info.Id
        self.DescriptionInfo.Description = description_info.Description
        self.DescriptionInfo.Icon = description_info.Icon


