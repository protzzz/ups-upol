# Korutiny
# Výraz yield a posílání hodnot do generátoru.
def test(x):
    print("Start")
    val = yield x + 1
    print("Hodnota:", val)

"""
>>> c = test(2)
>>> next(c)
Start
3
>>> c.send(3)
Hodnota: 3
StopIteration
"""

def add():
    yield (yield) + (yield)

"""
>>> c = add()
>>> next(c)
>>> c.send(1)
>>> c.send(3)
4
"""

def sum_vals(n):
    result = 0
    for i in range(n):
        v = yield result
        result = result + v
    yield result


"""
>>> c = sum_vals(3)
>>> next(c)
0
>>> c.send(1)
1
>>> c.send(3)
4
>>> c.send(5)
9
>>> next(c)
StopIteration
"""
