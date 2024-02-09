def double(x):
    return x + x

"""
>>> double(double(2))
8
"""

def apply_twice(f, x):
    return f(f(x))

"""
>>> apply_twice(double, 2)
8
"""

def twice(f):
    return lambda x: f(f(x))

"""
>>> twice(double)(2)
8
"""

quadruple = twice(double)

"""
>>> quadruple(2)
8
"""

def sub(m):
    return lambda n: m - n

"""
>>> sub(5)(3)
2
"""

def swap(f):
    return lambda x: lambda y: f(y)(x)

"""
>>> swap(sub)(5)(3)
-2
"""

def comp(f, g):
    return lambda x: f(g(x))

"""
>>> comp(sub(2), sub(3))(1)
0
"""

def twice2(f):
    return comp(f, f)

"""
>>> twice2(double)(2)
8
"""

# Fibonacciho posloupnost
def fib(n):
    return 0 if n == 0 else (1 if n == 1 else fib(n - 1) + fib(n - 2))

"""
>>> fib(5)
5
>>> fib(50) # trvá dlouho
"""

# Efektivnější iterativní verze:
def fib_iter(a, b, n):
    return a if n == 0 else fib_iter(b, a + b, n - 1)

def fib2(n):
    return fib_iter(0, 1, n)

"""
>>> fib2(5)
5
>>> fib2(50)
12586269025
"""

# Výpočet:
"""
    fib2(3)
=== fib_iter(0, 1, 3)
=== fib_iter(1, 1, 2)
=== fib_iter(1, 2, 1)
=== fib_iter(2, 3, 0)
=== 2
"""
