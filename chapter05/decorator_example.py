def to_upper_case(func):
    """Convert to upper case and return to upper case."""

    # Adding this line, will call passed function to get text
    text = func()

    if not isinstance(text, str):
        raise TypeError("Not a string type")
    return text.upper()


@to_upper_case
def say():
    return "welcome"

say()      # WELCOME
