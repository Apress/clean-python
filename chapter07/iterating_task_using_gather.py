import asyncio


async def is_odd(data):
    odd_even = []
    for item in data:
        odd_even.append((item, "Even") if item % 2 == 0 else (item, "Odd"))
    await asyncio.sleep(1)
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
    await asyncio.sleep(1)
    return primes


async def main(data):
    odd_task = asyncio.create_task(is_odd(data))
    prime_task = asyncio.create_task(is_prime(data))
    compl = await asyncio.gather(odd_task, prime_task)
    print(f"completed with data: {compl}")
    return compl



"""
Result
asyncio.run(main([3, 5, 10, 23, 90]))
completed with data:
[[(3, 'Odd'), (5, 'Odd'), (10, 'Even'), (23, 'Odd'), (90, 'Even')], [(3, 'Prime'), (3, 'Not Prime'), (10, 'Not Prime'), (90, 'Not Prime'), (90, 'Not Prime')]]
"""