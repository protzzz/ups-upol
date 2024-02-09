from co import *
x = None

def p1():
    global x
    random_sleep()
    x = 1


def p2():
    global x
    random_sleep()
    x = 2

co_call(p1, p2)
print(x) # Dostáváme různé výsledky.
