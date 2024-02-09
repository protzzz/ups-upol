from fmw import *

# Dvakrát použité tlačítko:
"""
moved(button("OK"), 30, 40)
button_ok = button("OK")
g1 = group(button_ok, moved(button_ok, 30, 40))
display_window(g1)
"""

# Skupina tří přepínačů:
"""
r1 = radiobutton(True)
r2 = moved(radiobutton(False), 0, 30)
r3 = moved(radiobutton(False), 0, 60)
g2 = group(r1, group(r2, r3))
display_window(g2)
"""

# Skupina tří přepínačů s volitelným rozestupem:

def radiobutton_group3(d):
    return group(radiobutton(True),
                 moved(group(radiobutton(False),
                             moved(radiobutton(False),
                                   0,
                                   d)),
                       0,
                       d))

"""
display_window(radiobutton_group3(20))
display_window(group(radiobutton_group3(20),
                     moved(radiobutton_group3(40), 50, 0)))
"""

# Hodnotu výrazu můžeme zobrazit:
"""
>>> group(radiobutton_group3(20),
          moved(radiobutton_group3(40), 50, 0))
group(group(radiobutton(True),
            moved(group(radiobutton(False),
                        moved(radiobutton(False), 0, 20)),
                  0,
                  20)),
      moved(group(radiobutton(True),
                  moved(group(radiobutton(False),
                              moved(radiobutton(False),0,40)),
                        0,
                        40)),
            50,
            0))
>>> display_window(group(group(radiobutton(True),
                               moved(group(radiobutton(False),
                                           moved(radiobutton(False), 0, 20)),
                                     0,
                                     20)),
                         moved(group(radiobutton(True),
                                     moved(group(radiobutton(False),
                                                 moved(radiobutton(False), 0, 40)),
                                           0,
                                           40)),
                               50,
                               0)))
"""


# Volitelný počet přepínačů:
def radiobutton_group(n, d):
    return (radiobutton(False)
            if n == 1
            else group(radiobutton(False),
                       moved(radiobutton_group(n - 1, d),
                             0,
                             d)))
"""
display_window(radiobutton_group(5, 20))
"""

# Úkol 1: Přepínač s popiskem.
# labeled_radiobutton(False, "A")

# Úkol 2: Skupina přepínačů s popisky.
#         Popisky zadáme seznamem řetězců.
#
# labeled_radiobutton_group(cons("A", cons("B", cons("C", empty))), 20)
