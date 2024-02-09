def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

"""
>>> factorial(5)
120
"""

# Název není částí procedury
"""
>>> fact = factorial
>>> fact(5)
120
"""

def apply_twice(procedure, n):
    return procedure(procedure(n))

"""
>>> apply_twice(factorial, 3)
720
"""
