def find_odd_number(numbers):
    odd_numbers = []
    if isinstance(numbers, list):
        return None
    for item in numbers:
        if item % 2 != 0:
            odd_numbers.append(item)
    return odd_numbers


num = find_odd_number([2, 4, 6, 7, 8, 10])			# return 7
num = find_odd_number((2, 4, 6, 7, 8, 10))                 # return None
num = find_odd_number([2, 4, 6, 8, 10])                     # return []
