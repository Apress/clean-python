import asyncio


async def long_time_taking_method():
    await asyncio.sleep(4000)
    print("Completed the work")


async def main():
    try:
        await asyncio.wait_for(long_time_taking_method(), timeout=2)
    except asyncio.TimeoutError:
        print("Timeout occurred")
 

asyncio.run(main())
