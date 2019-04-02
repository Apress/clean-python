from functools import wraps


def logging(func):
    @wraps(func)
    def logs(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return logs


@logging
def foo(x):
    """does some math"""
    return x + x * x


print(foo.__name__)  # prints 'f'
print(foo.__doc__)   # prints 'does some math'
