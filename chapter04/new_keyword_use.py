from abc import abstractmethod, ABCMeta

class UserAbstract(metaclass=ABCMeta):
    """Abstract base class template, implimenting factory pattern using __new__() initializer."""

    def __new__(cls, *args, **kwargs):
        """Creates an object instance a sets a base property."""
        obj = object.__new__(cls)
        obj.base_property = "Adding Property for each subclass"
        return obj


class User(UserAbstract):
    """Implement UserAbstract class and add its own variable."""

    def __init__(self):
        self.name = "Larry"


user = User()
user.name
# Larry
user.base_property
# Adding Property for each subclass
