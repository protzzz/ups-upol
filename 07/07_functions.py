# Definice základních funkcí:
def succ(x):
    return x + 1

def pred(x):
    return x - 1

def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

def negation(x):
    return not x

def apply_to_two(f):
    return f(2)

succ2 = lambda x: x + 1

def const_2(x):
    return 2

def const(x):
    return lambda y: x

const_3 = const(3)

const2 = lambda x: lambda y: x

def add(x):
    return lambda y: x + y

add_3 = add(3)

add2 = lambda x: lambda y: x + y

def comp(f, g):
    return lambda x: f(g(x))

succ_square = comp(succ, square)
square_succ = comp(square, succ)

comp2 = lambda f, g: lambda x: f(g(x))

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)
