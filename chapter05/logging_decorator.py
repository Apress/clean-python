def logging(func):
    def logs(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return logs


@logging
def foo(x):
    """Calling function for logging"""
    return x * x


fo = foo(10)
print(foo.__name__)        #  logs
