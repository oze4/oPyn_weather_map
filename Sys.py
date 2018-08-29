class Sys(object):
    Type = str()
    Id = str()
    Message = int()
    Country = str()
    Sunrise = str()
    Sunset = str()

    def __init__(self, _type, _id, message, country, sunrise, sunset):
        self.Type = _type
        self.Id = _id
        self.Message = message
        self.Country = country
        self.Sunrise = sunrise
        self.Sunset = sunset

