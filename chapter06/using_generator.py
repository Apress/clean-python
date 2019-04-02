def generate_numbers(limit):
    for item in range(limit):
        yield item*item
        print(f"Inside the yield: {item}")


numbers = generate_numbers() # create a generator

print(numbers) # numbers is an object!
# <generator object generate_numbers at 0xb7555c34>

for item in numbers:
     print(item)
