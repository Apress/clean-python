class MultipleByTwo:
    def __init__(self, num, limit):
        self.num = num
        self.limit = limit
        self.counter = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        value = self.number * self.counter

        if value > self.limit:
            raise StopIteration
        else:
          return value


for num in MutlipleByTwo(500, 5000):
    print(num)
