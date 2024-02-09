

def memory():
    old = None
    val = yield
    
    while True:
        tmp = yield old
        old = val
        val = tmp


"""
>>> c = memory()
>>> next(c)
>>> c.send(5)
>>> c.send(4)
5
>>> c.send(3)
4
>>> c.send(10)
3
"""
