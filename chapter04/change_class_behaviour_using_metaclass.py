class NoClassInstance:
    """Create the user object."""
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly""")


class User(metaclass=NoClassInstance):

    @staticmethod
    def print_name(name):
        """print name of the provided value."""
        print(f"Name: {name}")


user = User()
# TypeError: Can't instantiate directly
User.print_name("Larry Page")
# Name: Larry Page
