class MutipleByTwo:
    def __init__(self, number):
        self.number = number
        self.count = 0

    def __next__(self):
        self.count += 1
        return self.number * self.count


mul = MutipleByTwo(500)
print(next(mul))    # 500
print(next(mul))    # 1000
print(next(mul))    # 1500
