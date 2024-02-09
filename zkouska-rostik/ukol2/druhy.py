import aio
import random

storage = aio.Storage()
storage.set_max_delay(3)

async def log_set(storage, key, value):
    print("Storing:", key, value)
    try:
        await storage.set(key, value)
        print("Stored:", key, value)
    except RuntimeError as e:
        print("Storage error while loading the data")

async def query_data():
    while True:
        try:
            value = await storage.get("data")
            print("Query Coroutine: Received value from storage:", value)
            await aio.random_sleep(1) 
        except RuntimeError as e:
            print("Query Coroutine: Storage error -", e)

async def update_data():
    await aio.random_sleep(random.randint(3, 20))
    try:
        await storage.set("data", 2)
        print("Update Coroutine: Value in storage changed to 2")
    except RuntimeError as e:
        print("Update Coroutine: Storage error -", e)

async def main():
    await log_set(storage, "data", 1)
    query_task = aio.arun(query_data())
    update_task = aio.arun(update_data())
    await update_task
    await query_task

aio.run(main())
