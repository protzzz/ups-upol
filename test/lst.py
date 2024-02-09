# (Spojové) seznamy

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


# Další funkce:
def list_nth(lst, i):
    return first(lst) if i == 0 else list_nth(rest(lst), i - 1)

def list_range(m, n):
    return empty if m >= n else cons(m, list_range(m + 1, n))

def length(lst):
    return 0 if is_empty(lst) else 1 + length(rest(lst))

def list_map(function, lst):
    return (empty
            if is_empty(lst)
            else cons(function(first(lst)),
                      list_map(function, rest(lst))))

def is_member(val, lst):
    return (not is_empty(lst)
            and (first(lst) == val or is_member(val, rest(lst))))

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
        
def list_reduce(function, init, lst):
    return (init
            if is_empty(lst)
            else function(first(lst),
                          list_reduce(function,
                                      init,
                                      rest(lst))))

def list_change(lst, index, value):
    return (cons(value, rest(lst))
            if index == 0
            else cons(value, list_change(rest(lst), index - 1, value)))

def list_change_el(lst, index, value):
    return (cons(value, rest(lst))
            if index == 0
            else cons(first(lst), list_change_el(rest(lst), index - 1, value)))
            
def list_change(lst, index, function):
    return (cons(function(first(lst)), rest(lst))
            if index == 0
            else cons(first(lst), list_change(rest(lst), index - 1, function)))
    
def list_constant(length, value):
    if length == 0:
        return empty
    else:
        return cons(value, list_constant(length - 1, value))
