# Přímé vytvoření procesu
from co import *

x = None

def p():
    global x
    random_sleep()
    x = 1
    
process = start_process(p)
random_sleep()
x = 2
join_process(process)
# Zde už program není paralelní:
print(x)

