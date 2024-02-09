# Seznamy.

# Prázdný seznam:
empty = []

# Seznam je buď prázdný, nebo vznikne přidáním prvku
# na začátek seznamu.

def cons(val, lst):
    """Přidá prvek na začátek seznamu."""
    return [val, lst]

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1]
# Platí:
"""
    first(cons(val, lst))
=== val

    rest(cons(val, lst))
=== lst
"""

# Testovací seznam:
test_lst = cons(1, cons(2, cons(3, empty)))

"""
>>> first(test_lst)
1
>>> rest(test_lst)
[2, [3, []]]
"""

# Test prázdnosti:

def is_empty(lst):
    return lst == empty

# Platí:
"""
    is_empty(EMPTY)
=== True

    is_empty(cons(val, lst))
=== False
"""

# Testy:
"""
>>> is_empty(EMPTY)
True
>>> is_empty(test_lst)
False
>>> is_empty(rest(rest(rest(test_lst))))
True
"""

# Druhý prvek seznamu

"""
>>> first(rest(test_lst))
2
"""

def second(lst):
    return first(rest(lst))

"""
>>> second(test_lst)
2
"""

"""
    second(test_lst)
=== second(cons(1, cons(2, cons(3, EMPTY))))
=== first(rest(cons(1, cons(2, cons(3, EMPTY)))
=== first(cons(2, cons(3, EMPTY)))
=== 2
"""


"""
>>> second(rest(test_lst))
3
"""

def comp(f, g):
    return lambda x: f(g(x))

second2 = comp(first, rest)

"""
>>> second2(test_lst)
2
"""
