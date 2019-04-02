import asyncio
import time


async def say_something(delay, words):
    print(f"Before: {words}")
    await asyncio.sleep(delay)
    print(f"After: {words}")
 

async def main():
    print(f"Starting Tasks: {time.strftime('%X')}")
    task1 = asyncio.create_task(say_something(1, "First task started"))
    task2 = asyncio.create_task(say_something(2, "Second task started"))
 
    await task1
    await task2
 
    print(f"Finished Tasks: {time.strftime('%X')}")
 
 
asyncio.run(main())

"""
Result:
Starting Tasks: 11:43:56
Before: First task started
Before: Second task started
After: First task started
After: Second task started
Finished Tasks: 11:43:58
"""
