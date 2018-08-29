import CityCoordinate
import Clouds
import DescriptionInfo
import Measurements
import Sys
from Wind import Wind as WindInfo


class Summary(object):
    Timestamp = str()
    Weather_Id = str()
    City = str()
    Code = str()
    Visibility = str()
    Base_ = str()
    Date_Time = str()
    Wind = WindInfo()
    _Sys_ = Sys
    _Measurements_ = Measurements
    _DescriptionInfo_ = DescriptionInfo
    _Clouds_ = Clouds
    _CityCoordinate_ = CityCoordinate

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
        self.Sys.Sys.Country = sys.Country
        self.Sys.Sys.Id = sys.Id

