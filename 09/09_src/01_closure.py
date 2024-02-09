# Lexikální uzávěry
#
# Prostředí udává hodnoty proměnných.
# Například:
#
# x | 1
# y | 2

# Prostředí může mít rodiče,
# kterým je opět prostředí.
#
# Jediné prostředí,
# které nazýváme globální prostředí,
# nemá žádného rodiče.
#
# Zjišťování hodnoty proměnné X v prostředí E
# probíhá následovně:
#
# 1. Pokud prostředí E udává hodnotu V proměnné X,
#    pak je V výsledkem.
# 2. Pokud prostředí E neudává hodnotu proměnné X,
#    ale má rodiče EP,
#    pak je výsledek hodnota proměnné X
#    v prostředí EP.
# 3. Jinak proměnná X nemá hodnotu v prostředí E.

# Každá funkce je určena:
# 1. parametry,
# 2. tělem,
# 3. prostředím vzniku.

# Například:

def f(x, y):
    return x + y

# funkce f je určena:
# 1. parametry x, y
# 2. tělem x + y
# 3. prostředí vzniku je globální prostředí


# Vykonávání kódu probíhá vzhledem k prostředí.
# Například vyhodnocení výrazu
#
# x + y
#
# povede v prostředí:
#
# x | 1
# y | 2
#
# k hodnotě 3.

# Při zavolání funkce se nejprve vytvoří prostředí E,
# kde parametry funkce budou mít hodnoty argumentů.
# Rodičem prostředí E bude prostředí vzniku funkce.
# Poté se vykoná tělo funkce v prostředí E.
#
# Například:
#
# f(1, 2)
#
# způsobí vytvoření prostředí E:
#
# x | 1
# y | 2
#
# Rodičem prostředí E je globální prostředí
# (prostředí vzniku funkce f).
#
# Poté se v prostředí E vykoná tělo funkce:
#
# return x + y
#
# Vykonání ukončí volání funkce s hodnotou 3.
#
# Pokud při vykonávání kódu v prostředí E vznikne funkce,
# pak tato funkce bude mít prostředí vzniku E.
#
# Například:

def g(y):
    def h(x):
        return x + y
    return h

# Zavoláním:

h1 = g(2)

# vznikne prostředí E1: 
#
# y | 2
#
# v kterém se vykoná:
#
# def h(x):
#    return x + y
# return h
#
# Funkce h bude mít prostředí vzniku E1
#
# Zavoláním:

h1(3)

# vznikne prostředí E2:
#
# x | 3
#
# Rodičem E2 bude prostředí vzniku h1
# tedy prostředí E1.
#
# V prostředí E2 se vykoná:
#
# return x + y
#
# Hodnota x se nalezne v prostředí E2
# a hodnota y v prostředí E1 (rodič E2).
#
# Výsledkem volání tedy bude 3.

def succ(x):
    return x + 1

def square(x):
    return x ** 2

def comp(f, g):
    return lambda x: f(g(x))

# Pomocí představených pravidel vyhodnoťte výraz:
"""
>>> comp(succ, square)(3)
10
"""
