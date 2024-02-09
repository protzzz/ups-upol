# Asynchronní úložiště
import aio

storage = aio.Storage()

async def log_set(storage, key, value):
    print("Storing:", key, value)
    await storage.set(key, value)
    print("Stored:", key, value)

async def log_get(storage, key):
    print("Loading:", key)
    value = await storage.get(key)
    print("Loaded:", key, value)
    return value
    

async def test_store():
    await log_set(storage, "name", "Anna")
    await log_set(storage, "age", 20)
    print("Received:", await log_get(storage, "name"))
    print("Received:",await log_get(storage, "age"))

"""
aio.run(test_store())
"""

"""
storage.set_max_delay(5)
aio.run(test_store())
"""

"""
storage.set_error_probability(0.2)
aio.run(test_store())
"""
