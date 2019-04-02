class Calculation:
    """
    A wrapper around the different calculation algorithms that allows to perform different action on two numbers.
    """
    def __init__(self, operation):
        self.operation = operation

    def __call__(self, first_number, second_number):
        if isinstance(first_number, int) and isinstance(second_number, int):
            return self.operation()
        raise ValueError("Provide numbers")
        

    
def add(self, first, second):
    return first + second

def multiply(self, first, second):
    return first * second


add = Calculation(add)
print(add(5, 4))         # 9
multiply = Calculation(multiply)
print(multiply(5, 4))       # 20
