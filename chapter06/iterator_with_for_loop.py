class MultipleByTwo:
    def __init__(self, num):
        self.num = num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.number * self.counter


for num in MutlipleByTwo(500):
    print(num)
