# Použití objektového a funkcionálního programování dohromady.
#
# Ve funkcionálním přístupu můžeme používat objekty,
# ale nesmíme je měnit.
#
# Všechny vlastnosti objektů jsou tedy jen pro čtení.

# Změníme reprezentaci seznamů z polí na objekty.

class List:
    pass

# Prázdný seznam:

class Empty(List):
    def is_empty(self):
        return True

    # Přepisujeme textovou reprezentaci:
    def __repr__(self):
        return "empty"


empty = Empty()

# Neprázdný seznam:
class NonEmpty(List):
    # Hodnoty vlastností zadáme při vytvoření:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def get_first(self):
        return self.first

    def get_rest(self):
        return self.rest

    def is_empty(self):
        return False
    
    # Přepisujeme textovou reprezentaci:
    def __repr__(self):
        return ("cons("
                + repr(self.get_first())
                + ", "
                + repr(self.get_rest())
                + ")")

    def __eq__(self, val):
        return (isinstance(val, NonEmpty)
                and self.get_first() == val.get_first()
                and self.get_rest() == val.get_rest())

"""
>>> cons(1, empty) == cons(1, empty)
True
"""


# Konstruktor:
def cons(val, lst):
    return NonEmpty(val, lst)

# Selektory:
def first(lst):
    return lst.get_first()

def rest(lst):
    return lst.get_rest()

# Test prázdnosti:
def is_empty(lst):
    return lst.is_empty()

test_lst = cons(1, cons(2, cons(3, cons(4, empty))))

# Seznam se tiskne pomocí cons a empty.
"""
>>> test_lst
cons(1, cons(2, cons(3, cons(4, empty))))
"""

# Zachovali jsme rozhraní k seznamům.
# Můžeme tedy použít libovolnou funkci napsanou
# dříve. Například:

def list_map(function, lst):
    return (empty
            if is_empty(lst)
            else cons(function(first(lst)),
                      list_map(function, rest(lst))))

"""
>>> list_map(lambda x: 2 ** x, test_lst)
cons(2, cons(4, cons(8, cons(16, EMPTY))))
"""
