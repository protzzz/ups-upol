y23# Paralelní počítadlo s uzamykáním
from co import *
x = 0
lock = make_lock()

def p():
    global x
    for i in range(100):
        with lock:
            random_sleep()
            tmp = x + 1
            random_sleep()
            x = tmp


co_call(p, p)
print(x)
