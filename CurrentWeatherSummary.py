import Clouds
import Sys
import Wind
import Measurements
import CityCoordinate
import DescriptionInfo


class CurrentWeatherSummary(object):

    def __init__(self,
                 timestamp, weather_id, city, code, visibility, base_, date_time,
                 clouds,
                 sys,
                 wind,
                 measurements,
                 city_coordinate,
                 description_info
                 ):
        self.Timestamp = timestamp
        self.Weather_Id = weather_id
        self.City = city
        self.Code = code
        self.Visibility = visibility
        self.Base_ = base_
        self.Date_Time = date_time
        self.Clouds = Clouds.Clouds(clouds.All)
        self.Sys = Sys.Sys(sys.Type, sys.Id, sys.Message,
                           sys.Country, sys.Sunrise, sys.Sunset)
        self.Wind = Wind.Wind(wind.Speed)
        self.Measurements = Measurements.Measurements(measurements.Temp, measurements.Pressure,
                                                      measurements.Humidity, measurements.Temp_Min,
                                                      measurements.Temp_Max)
        self.CityCoordinate = CityCoordinate.CityCoordinate(city_coordinate.Longitude, city_coordinate.Latitude)
        self.DescriptionInfo = DescriptionInfo.DescriptionInfo(description_info.Id, description_info.Main,
                                                               description_info.Description, description_info.Icon)
