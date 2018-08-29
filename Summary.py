import CityCoordinate
import Clouds
import DescriptionInfo
import Measurements
import Sys
import Wind


class Summary(CityCoordinate, Clouds, DescriptionInfo, Measurements, Sys, Wind):
    def __init__(self, timestamp, weather_id, city, code, visibility, base_, date_time):
        self.Timestamp = timestamp
        self.Weather_Id = weather_id
        self.City = city
        self.Code = code
        self.Visibility = visibility
        self.Base_ = base_
        self.Date_Time = date_time
