from decorator import decorator

@decorator
def trace(f, *args, **kw):
     kwstr = ', '.join('%r: %r' % (k, kw[k]) for k in sorted(kw))
     print("calling %s with args %s, {%s}" % (f.__name__, args, kwstr))
     return f(*args, **kw)

@trace
def func(): pass

func()
# calling func with args (), {}
