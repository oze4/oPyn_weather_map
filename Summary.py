from CityCoordinate import *
from Clouds import *
from DescriptionInfo import *
from Measurements import *
from Sys import *
from Wind import *


class Summary(object):

    def __init__(self, timestamp, weather_id, city, code, visibility, base_, date_time,
                 wind
                 ):
        # ~base params timestamp, weather_id, city, code, visibility, base_, date_time, ~params from 'Clouds' object
        # clouds_all, ~params from 'Wind' object wind_speed, ~params from 'Sys' object sys_type, sys_id, sys_message,
        #  sys_country, sys_sunrise, sys_sunset, ~params from 'Measurements' object measurement_temp,
        # measurement_pressure, measurement_humidity, measurement_temp_min, measurement_temp_max, ~params from
        # 'DescriptionInfo' object dscptn_info_id_, dscptn_info_main_, dscptn_info_description, dscptn_info_icon,
        # ~params from 'CityCoordinate' object city_coord_longitude, city_coord_latitude ):
        self.Timestamp = timestamp
        self.Weather_Id = weather_id
        self.City = city
        self.Code = code
        self.Visibility = visibility
        self.Base_ = base_
        self.Date_Time = date_time
        self.Wind.Speed = wind.Speed
