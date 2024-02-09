# Demonstrace, že x += 1 není atomické.
from co import *
import sys
from dis import dis

# Příkazy procesů se budou více prokládat:
sys.setswitchinterval(1e-10)

x = 0

def inc():
    global x
    x += 1

# Náhled do bajtkódu funkce inc:
"""
>>> dis(inc)
 10           0 RESUME                   0

 12           2 LOAD_GLOBAL              0 (x)
             12 LOAD_CONST               1 (1)
             14 BINARY_OP               13 (+=)
             18 STORE_GLOBAL             0 (x)
             20 RETURN_CONST             0 (None)
"""

def p():
    for i in range(100000):
        inc()
        


co_call(p, p)
print(x)

# Program spustíme v interpretu PyPy (https://www.pypy.org):
"""
% pypy3 08_counter.py 
196903
"""
