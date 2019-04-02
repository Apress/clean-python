class Temprature:
    def __init__(self, temprature=0):
        self.temprature = temprature

    @property
    def fahrenheit(self):
        return self._temprature
    
    @fahrenheit.setter
    def fahrenheit(self, temp):
        if not isinstance(temp, int):
            raise("Wrong input type")

        self._temprature = (self.temp * 1.8) + 32
