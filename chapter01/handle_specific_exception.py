def get_even_list(num_list):
    """Get list of odd numbers from given list."""
    # This can raise NoneType or TypeError exceptions
    return [item for item in num_list if item % 2 == 0]


numbers = None
try:
    get_even_list(numbers)
except TypeError:
    print("None Value has been provided.")
