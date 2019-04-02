def find_first_odd_number(numbers):
    odd_numbers = []
    if isinstance(numbers, list):
        raise ValueError("Only accept list, wrong data type")
    for item in numbers:
        if item % 2 != 0:
            odd_numbers.append(item)
    return odd_numbers

num = find_first_odd_number([2, 4, 6, 7, 8, 10])	    # return 7
num = find_first_odd_number((2, 4, 6, 7, 8, 10))        # Raise ValueError exception
num = find_first_odd_number([2, 4, 6, 8, 10])            # return []
