from co import *
import random

ITERATIONS = 5

def first_process(queue, semaphore):
    for i in range(ITERATIONS):
        number = random.randint(1, 100)
        safe_print(f"First process {i+1} sends number: {number}")
        queue.put(number)
        # ersemaphore.release()
        random_sleep()

def second_process(queue, result_queue, semaphore):
    process_count = 0
    while True:
        # semaphore.acquire()
        number1 = queue.get()
        number2 = queue.get()
        process_count += 1
        safe_print(f"Second process {process_count} is processing numbers: {number1}, {number2}")
        result = number1 + number2
        result_queue.put(result)

def third_process(result_queue):
    while True:
        result = result_queue.get()
        safe_print(f"Third process: Result {result}")


queue = Queue()
result_queue = Queue()
semaphore = Semaphore(0)

co_call(
    lambda: first_process(queue, semaphore),
    lambda: second_process(queue, result_queue, semaphore),
    lambda: third_process(result_queue)
)
