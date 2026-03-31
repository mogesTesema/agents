import asyncio
import time

async def generate():
    yield 1
    await asyncio.sleep(4)  # Simulate a blocking operation
    yield 2
    await asyncio.sleep(1)  # Simulate another blocking operation
    yield 3

async def main():
    async for x in generate():
        print(x)

asyncio.run(main())