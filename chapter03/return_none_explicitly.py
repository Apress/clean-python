def sum(first_number, second_number):
    if isinstance(first_number, int) and isinstance(second_number, int):
        return first_number + second_number
    else:
        return None


result = sum(10, "str")           # Return None
result = sum(10, 5)			 # Return 15
