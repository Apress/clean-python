def to_upper_case(func):
    """Convert to upper case and return to upper case."""

    # Adding this line, will call passed function to get text
    text = func()

    if not isinstance(text, str):
        raise TypeError("Not a string type")
    return text.upper()


def say():
    return "welcome"


def hello():
    return "hello"


to_upper_case(say)       # WELCOME

to_upper_case(hello)         # HELLO
