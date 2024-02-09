# Filtrování seznamu.

empty = []

def cons(val, lst):
    return [val, lst]

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1]

def is_empty(lst):
    return lst == empty


test_lst = cons(1, cons(2, cons(3, cons(4, empty))))

def list_filter(predicate, lst):
    return (
        empty
        if is_empty(lst)
        else (
            cons(first(lst), list_filter(predicate, rest(lst)))
            if predicate(first(lst))
            else list_filter(predicate, rest(lst))
            )
        )

def is_even(x):
    return x % 2 == 0
"""
>>> list_filter(is_even, test_lst)
[2, [4, []]]
>>> list_filter(lambda x: x % 2 == 1, test_lst)
[1, [3, []]]
"""
