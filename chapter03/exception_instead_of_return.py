def sum(first_number, second_number):
    if isinstance(first_number, int) and isinstance(second_number, int):
        return first_number + second_number
    else:
        raise ValueError("Provide only int values")
