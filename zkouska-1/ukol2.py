import aio
import random

class Counter:
    async def increase(self, storage):
        for _ in range(10):
            try:
                current_value = await storage.get("counter")
                await storage.set("counter", current_value + 1)
                print("Counter increased. Current value:", await storage.get("counter"))
            except RuntimeError as e:
                print("Error while increasing counter:", e)
                for _ in range(5):
                    await aio.random_sleep(1)
                    try:
                        current_value = await storage.get("counter")
                        await storage.set("counter", current_value + 1)
                        print("Counter increased (retry). Current value:", await storage.get("counter"))
                        break
                    except RuntimeError as e:
                        print("Error while increasing counter (retry):", e)

async def main():
    storage = aio.Storage()
    storage.set_max_delay(2)
    storage.set_error_probability(0.2)

    await storage.set("counter", 0)

    counter_instance = Counter()
    await counter_instance.increase(storage)

aio.run(main())
