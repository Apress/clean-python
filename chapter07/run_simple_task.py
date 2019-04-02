import asyncio


async def value(val):
    return val


async def main():
    # Creating a task to run concurrently
    # You can create as many task as possible here
    task = asyncio.create_task(value(89))
    
    # This will simply wait for task to finish
    await task
 

asyncio.run(main())
