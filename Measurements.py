class Measurements(object):

    def __init__(self):
        self.Temp = str()
        self.Pressure = str()
        self.Humidity = str()
        self.Temp_Min = str()
        self.Temp_Max = str()

    def set_measurements(self, temp, pressure, humidity, temp_min, temp_max):
        self.Temp = temp
        self.Temp_Max = temp_max
        self.Temp_Min = temp_min
        self.Pressure = pressure
        self.Humidity = humidity
