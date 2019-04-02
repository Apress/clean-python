import trio


async def greeting():
    await trio.sleep(1)
    return "Welcome to Trio!"

trio.run(greeting)

# Welcome to Trio!
