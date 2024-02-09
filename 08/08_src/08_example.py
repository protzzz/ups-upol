# Příklad
from fmw import *

def labels_range_from(m, n, d, y):
    return (empty_widget
            if m >= n
            else group(moved(label(str(m)), 0, y),
                       labels_range_from(m + 1, n, d, y + d)))

"""
>>> labels_range_from(1, 5, 30, 0)
group(moved(label('1'), 0, 0),
      group(moved(label('2'), 0, 30),
            group(moved(label('3'), 0, 60),
                  group(moved(label('4'), 0, 90),
                        empty_widget))))
"""

def labels_range(m, n, d):
    return labels_range_from(m, n, d, 0)

"""
>>> labels_range(1, 5, 30)
group(moved(label('1'), 0, 0),
      group(moved(label('2'), 0, 30),
            group(moved(label('3'), 0, 60),
                  group(moved(label('4'), 0, 90),
                        empty_widget))))
>>> display_window(labels_range(1, 5, 30))
"""
