# Paralelní počítadlo zjednodušené
from co import *
x = 0
lock = make_lock()

def p():
    global x
    for i in range(100):
        with lock:
            x = x + 1


co_call(p, p)
print(x)
