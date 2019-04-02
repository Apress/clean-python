import asyncio


async def gen_power_two(limit):
    item = 0
    while item < limit:
        yield 2 ** item
        item += 1
        await asyncio.sleep(1)


async def main(limit):
    gen = [item async for item in gen_power_two(limit)]
    return gen


print(asyncio.run(main(5)))
