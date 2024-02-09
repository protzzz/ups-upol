# Redukce seznamu.

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

def add(x, y):
    return x + y

def list_sum(lst):
    return 0 if is_empty(lst) else add(first(lst), list_sum(rest(lst)))

"""
>>> list_sum(test_lst)
10
"""

def list_reduce(function, init, lst):
    return (init
            if is_empty(lst)
            else function(first(lst),
                          list_reduce(function,
                                      init,
                                      rest(lst))))

"""
>>> list_reduce(add, 0, test_lst)
10
"""

def list_sum2(lst):
    return list_reduce(add, 0, lst)

"""
>>> list_sum2(test_lst)
10
"""

def mul(x, y):
    return x * y

"""
>>> list_reduce(mul, 1, test_lst)
24
"""

"""
>>> list_reduce(lambda el, res: res + 1, 0, test_lst)
4
"""


def list_map(function, lst):
    return list_reduce((lambda value, result:
                        cons(function(value), result)),
                       empty,
                       lst)

"""
>>> list_map(lambda x: x * x, test_lst)
[1, [4, [9, [16, []]]]]
"""



def list_filter(predicate, lst):
    return list_reduce((lambda value, result:
                        cons(value, result) if predicate(value) else result),
                       empty,
                       lst)


"""
>>> list_filter(lambda x: x % 2 == 0, test_lst)
[2, [4, []]]
"""
    

