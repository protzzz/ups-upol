# Předávání hodnoty pomocí fronty.

from co import *
from random import randint

buffer = Queue()

def producer():
    random_sleep(3)
    value = randint(0, 100)
    buffer.put(value)
    

def customer():
    value = buffer.get()
    safe_print(value)

co_call(producer, customer)
