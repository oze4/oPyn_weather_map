class Sys(object):

    def __init__(self):
        self.Type = str()
        self.Id = str()
        self.Message = int()
        self.Country = str()
        self.Sunrise = str()
        self.Sunset = str()

    def set_sys(self, type_, id_, message, country, sunrise, sunset):
        self.Type = type_
        self.Id = id_
        self.Message = message
        self.Country = country
        self.Sunrise = sunrise
        self.Sunset = sunset
