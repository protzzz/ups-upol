# Jednoduché předání hodnoty

from co import *
from random import randint

buffer = None

def producer():
    global buffer
    random_sleep(3)
    buffer = randint(0, 100)
    

def customer():
    while buffer == None:
        pass
    safe_print(buffer)

co_call(producer, customer)
