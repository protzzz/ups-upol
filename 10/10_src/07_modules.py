# Práce s iterátory:
import itertools

# Dokumentace:
# https://docs.python.org/3/library/itertools.html

# Například:
"""
>>> i = itertools.count(0)
>>> next(i)
0
>>> next(i)
1
>>> next(i)
2
"""

# Operátory jako funkce:
import operator

# Dokumentace:
# https://docs.python.org/3/library/operator.html

# Například:
"""
>>> operator.eq(1, 2)
False
>>> operator.add(1, 2)
3
"""

# Další funkce vyšších řádů:
import functools

# Dokumentace:
# https://docs.python.org/3/library/functools.html

# Například:
"""
>>> functools.reduce(operator.add, [1, 2, 3], 0)
6
"""
