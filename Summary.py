from Clouds import Clouds
from Sys import Sys
from Wind import Wind
from Measurements import Measurements
from CityCoordinate import CityCoordinate
from DescriptionInfo import DescriptionInfo


class Summary(object):

    def __init__(self,
                 timestamp, weather_id, city, code, visibility, base_, date_time,
                 clouds,
                 sys,
                 wind,
                 measurements,
                 citycoordinate,
                 descriptioninfo
                 ):
        self.Timestamp = timestamp
        self.Weather_Id = weather_id
        self.City = city
        self.Code = code
        self.Visibility = visibility
        self.Base_ = base_
        self.Date_Time = date_time
        self.Clouds = Clouds(clouds.All)
        self.Sys = Sys(sys.Type, sys.Id, sys.Message, sys.Country, sys.Sunrise, sys.Sunset)
        self.Wind = Wind(wind.Speed)
        self.Measurements = Measurements(measurements.Temp, measurements.Pressure,
                                         measurements.Humidity, measurements.Temp_Min, measurements.Temp_Max)
        self.CityCoordinate = CityCoordinate(citycoordinate.Longitude, citycoordinate.Latitude)
        self.DescriptionInfo = DescriptionInfo(descriptioninfo.Id, descriptioninfo.Main, descriptioninfo.Icon)
