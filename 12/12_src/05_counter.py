# Chybné paralelní počítadlo 
from co import *
x = 0

def p():
    global x
    for i in range(100):
        random_sleep()
        tmp = x + 1
        random_sleep()
        x = tmp


co_call(p, p)
print(x)
