# Rekurze na seznamech.

empty = []

def cons(val, lst):
    return [val, lst]

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1]

def is_empty(lst):
    return lst == empty

# Testovací seznam:
test_lst = cons(1, cons(2, cons(3, empty)))

# Délka seznamu.
def length(lst):
    return (0
            if is_empty(lst)
            else 1 + length(rest(lst)))

"""
>>> length(empty)
0
>>> length(test_lst)
3
>>> length(rest(test_lst))
2
"""

# Test příslušnosti prvku do seznamu.
def is_member(val, lst):
    return (not is_empty(lst)
            and (first(lst) == val
                 or is_member(val, rest(lst))))

"""
>>> is_member(1, EMPTY)
False
>>> is_member(1, test_lst)
True
>>> is_member(3, test_lst)
True
>>> is_member(4, test_lst)
False
"""

# Seznam čísel.
def list_range(m, n):
    return empty if m >= n else cons(m, list_range(m + 1, n))

"""
>>> list_range(1, 5)
[1, [2, [3, [4, []]]]]
"""

# Každý prvek splňuje predikát.
def is_every(predicate, lst):
    return (is_empty(lst)
            or (predicate(first(lst))
                and is_every(predicate, rest(lst)))) 
"""
>>> is_every(lambda x: x > 2, cons(3, cons(5, empty)))
True
>>> is_every(lambda x: x > 2, cons(1, cons(5, empty)))
False
"""
