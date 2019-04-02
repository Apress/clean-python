class Memo(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = {}

    def __call__(self, _id, *args, **kwargs):
        if _id not in self.__cache:
            self.cache[_id] = super().__call__(_id, *args, **kwargs)
        else:
            print("Existing Instance")
        return self.__cache[id]


class Foo(Memo):
    def __init__(self, _id, *args, **kwargs):
        self.id = _id



def test():
    first = Foo(id="first")
    second = Foo(id="first")
    print(id(first) == id(second))

test()               # True
