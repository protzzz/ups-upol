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

    # Přepisujeme test rovnosti:
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
