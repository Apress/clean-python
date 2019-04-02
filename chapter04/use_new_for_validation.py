from abc import abstractmethod, ABCMeta


class UserAbstract(metaclass=ABCMeta):
    """Abstract base class template, implimenting factory pattern using __new__() initializer."""

    def __new__(cls, *args, **kwargs):
        """Creates an object instance a sets a base property."""
        obj = object.__new__(cls)
        given_data = args[0]
        # Validating the data here
        if not isinstance(given_data, str):
            raise ValueError(f"Please provide string: {given_data}")
        return obj


class User(UserAbstract):
    """Implement UserAbstract class and add its own variable."""

    def __init__(self, name):
        self.name = name


user = User(10)
# ValueError: Please provide string: 10
