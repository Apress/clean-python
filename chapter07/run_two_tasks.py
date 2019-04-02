import asyncio
import time


async def say_something(delay, words):
    print(f"Before: {words}")
    await asyncio.sleep(delay)
    print(f"After: {words}")
 
 
async def main():
    print(f"start: {time.strftime('%X')}")
 
    await say_something(1, "First task started.")
    await say_something(1, "Second ask started.")
 
    print(f"Finished: {time.strftime('%X')}")
 
 
asyncio.run(main())
"""
Result:
start: 11:30:11
Before: First task started.
After: First task started.
Before: Second ask started.
After: Second ask started.
Finished: 11:30:13
"""