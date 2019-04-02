class Person:
    def __init__(self, first_name, last_name):
        self.age = 50

    def get_name(self):
        return self.full_name


class Child(Person):
    def __init__(self):
        super().__init__()
        self.__age = 20


ch = Child()
print(ch.get())              # 50
print(ch.__age)              # 30