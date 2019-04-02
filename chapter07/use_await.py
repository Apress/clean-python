import asyncio


async def mult(first, second):
    print(f"Calculating multiply of {first} and {second}")
    await asyncio.sleep(1)
    num_mul = first * second
    print(f"Multiply of {num_mul}")
    return num_mul


async def sum(first, second):
    print(f"Calculating sum of {first} and {second}")
    await asyncio.sleep(1)
    num_sum = first + second
    print(f"Sum is {num_sum}")
    return num_sum


async def main(first, second):
    await sum(first, second)
    await mult(first, second)


asyncio.run(main(7, 8))

"""
Result
Calculating sum of 7 and 8
Sum is 15
Calculating multiply of 7 and 8
Multiply of 56
"""