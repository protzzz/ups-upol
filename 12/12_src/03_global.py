# Nastavení globální proměnné

x = 0

def f():
    x = 1

def g():
    global x
    x = 1
    
"""
>>> f()
>>> x
0
>>> g()
>>> x
1
"""
