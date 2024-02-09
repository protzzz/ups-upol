# Implementace spojových seznamů:
from lst import *

# Testovací seznam:
test_lst = cons(1, cons(2, cons(3, cons(4, empty))))

# Prvek na indexu:

def list_nth(lst, i):
    return first(lst) if i == 0 else list_nth(rest(lst), i - 1)

"""
>>> list_nth(test_lst, 2)
3
"""

# První prvek splňující predikát:
def list_find(pred, lst):
    return first(lst) if pred(first(lst)) else list_find(pred, rest(lst))

"""
>>> list_find(lambda x: x >= 2, test_lst)
2
>>> list_find(lambda x: x < 1, test_lst)
Error
"""

# První prvek splňující predikát (druhá verze):
def list_find2(pred, lst):
    return [] if is_empty(lst) else ([first(lst)]
                                     if pred(first(lst))
                                     else list_find2(pred, rest(lst)))

"""
>>> list_find2(lambda x: x >= 2, test_lst)
[2]
>>> list_find2(lambda x: x < 1, test_lst)
[]
"""

# Prvky na sudých indexech:
"""
>>> list_every_second(test_lst)
cons(1, cons(3, empty))
"""

# Poslední prvek:
"""
>>> list_last(test_lst)
4
"""

# Spojení seznamů:
"""
>>> list_append(cons(1, cons(2, empty)), cons(3, cons(4, empty)))
cons(1, cons(2, cons(3, cons(4, empty))))
"""

# Otočení pořadí prvků:
"""
>>> list_reverse(test_lst)
cons(4, cons(3, cons(2, cons(1, empty))))
"""

# Lze v předchozích příkladech použít redukce seznamu?
def list_reduce(function, init, lst):
    return (init
            if is_empty(lst)
            else function(first(lst),
                          list_reduce(function,
                                      init,
                                      rest(lst))))

"""
>>> list_reduce(lambda x, y: x + y, 0, test_lst)
10
"""
            
