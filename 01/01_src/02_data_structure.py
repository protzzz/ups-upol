# Datová struktura bod

"""
>>> p1 = [3, 4]
>>> p2 = [p1[0] + 1, p1[1] + 2]
>>> p2
[4, 6]
"""

def move_point(point, dx, dy):
    return [point[0] + dx, point[1] + dy]

"""
>>> p1 = [3, 4]
>>> p3 = move_point(p1, 1, 2)
>>> p3
[4, 6]
"""
