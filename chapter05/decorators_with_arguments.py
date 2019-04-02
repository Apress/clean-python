def to_upper_case(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()
    return wrapper


@to_upper_case
def say(greet):
    return greet


say("hello, how you doing")     # 'HELLO, HOW YOU DOING'
