# Generátor


def get_numbers():
    i = 0
    while i < 3:
        yield i
        i = i + 1

# Zavolání generátoru vrátí iterátor.

"""
>>> i = get_numbers()
"""

# Vykonávání těla generátoru se spustí až funkcí next:

"""
>>> next(i)
0
"""

# Vykonání příkazu yield vyprodukuje prvek iterátoru a pozastaví vykonávání
# těla generátoru.

"""
>>> next(i)
1
>>> next(i)
2
"""

# Pokud vykonávání těla generátoru skončí, vyvolá se výjimka StopIteration.

"""
>>> next(i)
StopIteration
"""

def get_numbers2():
    print("Start")
    i = 0
    while i < 3:
        print("Compute", i)
        yield i
        i = i + 1
    print("End")

"""
>>> i = get_numbers2()
>>> next(i)
Start
Compute 0
0
>>> next(i)
Compute 1
1
>>> next(i)
Compute 2
2
>>> next(i)
End
StopIteration
"""

# Funkce map a filter můžeme napsat jako generátory.

def gmap(function, iterable):
    for value in iterable:
        yield function(value)


def square(x):
    return x ** 2

"""
>>> i = gmap(square, [1, 2, 3])
>>> next(i)
1
>>> next(i)
4
>>> next(i)
9
>>> next(i)
StopIteration
"""


def gfilter(predicate, iterable):
    for value in iterable:
        if predicate(value):
            yield value

def is_even(x):
    return x % 2 == 0

"""
>>> i = gfilter(is_even, range(5))
>>> next(i)
0
>>> next(i)
2
>>> next(i)
4
>>> next(i)
StopIteration
"""

# Prvky iterátoru nemusí nikdy dojít.

def get_numbers():
    n = 0
    while True:
        yield n
        n += 1

"""
>>> i = get_numbers()
>>> next(i)
0
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
"""


# Tisk prvků get_numbers() vede k nekonečnému vykonávání.
"""
>>> for i in get_numbers():
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
...
"""

# Nekonečné iterátory můžeme filtrovat i mapovat.

"""
>>> i = map(lambda x: x ** 2, get_numbers())
>>> next(i)
0
>>> next(i)
1
>>> next(i)
4
>>> next(i)
9
"""

"""
>>> i = filter(lambda x: x % 2 == 0, get_numbers())
>>> next(i)
0
>>> next(i)
2
>>> next(i)
4
"""

"""
>>> i = map(lambda x: x ** 2,filter(lambda x: x % 2 == 0, get_numbers()))
>>> next(i)
0
>>> next(i)
4
>>> next(i)
16
>>> next(i)
36
"""
