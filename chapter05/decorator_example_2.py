def to_upper_case(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()
    return wrapper 


@to_upper_case
def say():
    return "welcome"


@to_upper_case
def hello():
    return "hello"


say()       # WELCOME
hello()     # HELLO
