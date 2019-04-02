import trio


async def is_odd(data):
    odd_even = []
    for item in data:
        odd_even.append((item, "Even") if item % 2 == 0 else (item, "Odd"))
    await trio.sleep(1)
    return odd_even


async def is_prime(data):
    primes = []
    for item in data:
        if item <= 1:
            primes.append((item, "Not Prime"))
        if item <= 3:
            primes.append((item, "Prime"))
        if item % 2 == 0 or item % 3 == 0:
            primes.append((item, "Not Prime"))
        factor = 5
        while factor * factor <= item:
            if item % factor == 0 or item % (factor + 2) == 0:
                primes.append((item, "Not Prime"))
            factor += 6
    await trio.sleep(1)
    return primes
 
 
async def main(data):
    print("Calculation has started!")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(is_odd, data)
        nursery.start_soon(is_prime, data)

trio.run(main, [3, 5, 10, 23, 90])
