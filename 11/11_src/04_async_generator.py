# Asynchronní generátory
import aio

# Asynchronní posloupnost:
async def delay_range(n):
    for i in range(n):
        await aio.random_sleep(1)
        yield i

async def process(agen):
    # Procházení asynchronní posloupností:
    async for i in agen:
        print(i)

async def main():
    promise1 = aio.arun(process(delay_range(5)))
    promise2 = aio.arun(process(delay_range(10)))
    await promise1
    await promise2

aio.run(main())
