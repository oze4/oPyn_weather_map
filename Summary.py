class Summary(object):

    def __init__(self):
        self.Timestamp = str()
        self.Weather_Id = str()
        self.City = str()
        self.Code = str()
        self.Visibility = str()
        self.Base_ = str()
        self.Date_Time = str()

    def set_summary(self, timestamp, weather_id, city, code, visibility, base_, date_time):
        self.Timestamp = timestamp
        self.Weather_Id = weather_id
        self.City = city
        self.Code = code
        self.Visibility = visibility
        self.Base_ = base_
        self.Date_Time = date_time
