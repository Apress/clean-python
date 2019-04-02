from abc import ABCMeta, abstractmethod

class Fruite(metaclass=ABCMeta):

    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple:
    def originated(self):
        return "Central Asia"


fruite = Fruite("apple")
"""
TypeError:
"Can't instantiate abstract class concrte with abstract method taste"
"""
