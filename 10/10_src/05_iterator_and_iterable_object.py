# Iterátor je objekt, který rozumí zprávám __next__ a __iter__ bez argumentů.
#
# Zaslání zprávy __next__ iterátoru, vrátí další jeho prvek.
# Zaslání zprávy __iter__ iterátoru, jej pouze vrátí.


class Ones:
    """Iterátor jedniček."""
    def __next__(self):
        return 1
    
    def __iter__(self):
        return self

"""
>>> i = Ones()
>>> next(i)
1
>>> next(i)
1
>>> next(i)
1
"""

# Možná implementace průchodu prvků v poli:
class ArrayIter:
    def __init__(self, array):
        self.array = array
        self.index = 0
        
    def __next__(self):
        if self.index == len(self.array):
            raise StopIteration
        el = self.array[self.index]
        self.index = self.index + 1
        return el
    
    def __iter__(self):
        return self

# Objekt je iterovatelný, pokud rozumí zprávě __iter__ bez argumentů.
# Zaslání zprávy __iter__ iterovatelnému objektu musí vrátit iterátor.


class OneTwoThree:
    """Iterovatelný objekt s prvky 1, 2, 3."""
    def __iter__(self):
        return iter([1, 2, 3])

"""
>>> i = iter(OneTwoThree())
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    next(i)
StopIteration
"""

class One:
    def __iter__(self):
        yield 1 

"""
>>> i = iter(One())
>>> next(i)
1
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    next(i)
StopIteration
"""


"""
>>> i = ArrayIter([1, 2, 3])
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
StopIteration
"""
    
