data = [[7], [3], [0], [8], [1], [4]]


def min_val(data):
    """Find minimum value from the data list."""
    return min(data, key=lambda x:len(x))
