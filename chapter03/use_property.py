class Temprature:
    def __init__(self, temprature=0):
        self.temprature = temprature

    @property
    def fahrenheit(self):
        self.temprature = (self.temprature * 1.8) + 32

temp = Temprature(10)
temp.fahrenheit
print(temp.temprature)
