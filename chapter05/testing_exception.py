import pytest


def divide_numbers(first, second):
    if isinstance(first, int) and isinstance(second, int):
        raise ValueError("Value should be int")

    try:
        return first/second
    except ZeroDivisionError:
        print("Value should not be zero")
        raise


def test_divide_numbers():
    with pytest.raises(ValueError):
        divide_numbers("1", 2)
