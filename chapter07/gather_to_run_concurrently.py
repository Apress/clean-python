import asyncio
import time

async def greetings():
    print("Welcome")
    await asyncio.sleep(1)
    print("Good By")
 
async def main():
    await asyncio.gather(greetings(), greetings())
 
def say_greet():
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Total time elapsed: {elapsed}")
 
asyncio.run(say_greet())
