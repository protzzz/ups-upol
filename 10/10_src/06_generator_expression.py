# Generující výrazy
"""
>>> i = (x + 1 for x in [1, 4, 2, 3] if x % 2 == 0)
>>> next(i)
5
>>> next(i)
3
>>> next(i)
StopIteration
>>> list(x ** 2 for x in range(5))
[0, 1, 4, 9, 16]
>>> list([x, y] for x in range(4) for y in range(x))
[[1, 0], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]]
>>> [[x, y] for x in range(4) for y in range(x)]
[[1, 0], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]]
>>> [[x, y] for x in range(1, 10) for y in range(2, x) if x % y == 0]
[[4, 2], [6, 2], [6, 3], [8, 2], [8, 4], [9, 3]]
"""
