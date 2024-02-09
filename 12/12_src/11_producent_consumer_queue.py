# Opakované předávání hodnot pomocí fronty.

from co import *
from random import randint

items = Queue()

def producer():
    for i in range(10):
        random_sleep(1)
        items.put(i)
    items.put(None)
    

def customer():
    while True:
        value = items.get()
        if value == None:
            return None
        random_sleep(1)
        safe_print(value)

co_call(producer, customer)
