# Mapování seznamu.

empty = []

def cons(val, lst):
    return [val, lst]

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1]

def is_empty(lst):
    return lst == empty

test_lst = cons(1, cons(2, cons(3, empty)))

def succ(x):
    return x + 1

def list_map_succ(lst):
    return empty if is_empty(lst) else cons(succ(first(lst)),
                                            list_map_succ(rest(lst)))

"""
>>> list_map_succ(test_lst)
[2, [3, [4, []]]]
"""

def square(x):
    return x * x

def list_map_square(lst):
    return empty if is_empty(lst) else cons(square(first(lst)),
                                            list_map_square(rest(lst)))

"""
>>> list_map_square(test_lst)
[1, [4, [9, []]]]
"""

def list_map(function, lst):
    return (empty
            if is_empty(lst)
            else cons(function(first(lst)),
                      list_map(function, rest(lst))))

"""
>>> list_map(square, test_lst)
[1, [4, [9, []]]]
>>> list_map(succ, test_lst)
[2, [3, [4, []]]]
>>> list_map(lambda x: x - 1, test_lst)
[0, [1, [2, []]]]
"""
