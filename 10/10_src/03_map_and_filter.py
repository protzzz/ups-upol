# Vestavěná funkce map očekává
# funkci F jednoho parametru
# a iterovatelnou hodnotu.
# 
# Funkce map nejprve vytvoří
# iterátor pro iterovatelnou hodnotu.
# Poté vrátí iterátor
# návratových hodnot
# volání funkce F na prvky iterátoru.

def succ(x):
    return x + 1

"""
>>> i = map(succ, [1, 2, 3])
>>> next(i)
2
>>> next(i)
3
>>> next(i)
4
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    next(i)
StopIteration
"""

# Návratová hodnota map je iterovatelná hodnota.
# Můžeme ji použít
# jako druhý argument další funkce map.

def square(x):
    return x * x

"""
>>> i = map(square, map(succ, [1, 2, 3]))
>>> next(i)
4
>>> next(i)
9
>>> next(i)
16
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    next(i)
StopIteration
"""

# Funkce F se zavolá až při získání další hodnoty.

def succ2(x):
    print("call succ2", x)
    return x + 1

"""
>>> i = map(succ2, [1, 2, 3])
>>> next(i)
call succ2 1
2
>>> next(i)
call succ2 2
3
>>> next(i)
call succ2 3
4
>>> next(i)
StopIteration
"""

"""
>>> list(map(lambda x: x ** 2, range(3)))
[0, 1, 4]
"""

# Funkci map lze použít i na více posloupností:

"""
>>> list(map(lambda x, y: x + y, range(5), range(0, 10, 2)))
[0, 3, 6, 9, 12]
"""

def is_even(x):
    return x % 2 == 0

# Vestavěná funkce filter:
"""
>>> i = filter(is_even, [1, 2, 3, 4, 5, 6])
>>> next(i)
2
>>> next(i)
4
>>> next(i)
6
>>> next(i)
StopIteration
>>> for x in filter(is_even, [1, 2, 3, 4, 5, 6]):
	print(x)

	
2
4
6

>>> list(filter(is_even, [1, 2, 3, 4, 5, 6]))
[2, 4, 6]
"""

