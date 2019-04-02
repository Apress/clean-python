import asyncio


async def generator(limit):
    for item in range(limit):
        yield item
        await asyncio.sleep(1)


async def main():
    async for item in generator(10):
        print(item)


asyncio.run(main())
