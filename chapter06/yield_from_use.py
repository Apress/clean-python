def flat_list(iter_values):
    """flatten a multi list or something."""
    for item in iter_values:
        if hasattr(item, '__iter__'):
            yield from flat_list(item)
        else:
            yield item

print(list(flat_list([1, [2], [3, [4]]])))
#  [1, 2, 3, 4]
