import curio

async def generate(limit):
    step = 0
    while step <= limit:
        await curio.sleep(1)
        step += 1

if __name__ == "__main__":
    curio.run(generate, 10)
