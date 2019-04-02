import curio


async def generate(limit):
    step = 0
    while step <= limit:
        await curio.sleep(1)
        step += 1


async def say_hello():
    print("Hello")
    await curio.sleep(1000)


async def main():
    hello_task = await curio.spawn(say_hello)
    await curio.sleep(3)

    gen_task = await curio.spawn(generate, 5)
    await gen_task.join()

    print("Welcome")
    await hello_task.join()
    print("Good by")


if __name__ == '__main__':
    curio.run(main)
