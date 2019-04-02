def add_prefix(func):
    def wrapper():
        text = func()
        result = " ".join([text, "Larry Page!"])
        return result
    return wrapper


def to_upper_case(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()
    return wrapper


@to_upper_case
@add_prefix
def say():
    return "welcome"


say()      #   WELCOME LARRY PAGE!
