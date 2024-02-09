# Základní práce s objekty

from omw import *

# Zatím nevysvětlujeme:
window = Window()
label = Label()
window.set_widget(label)

# Objekt label
"""
>>> label
<omw.Label object at 0x11065fe50>
"""

# Zasílání zpráv
"""
>>> label.set_text("Pomeranč")
<omw.Label object at 0x11065fe50>
>>> label.get_text()
'Pomeranč'
"""

# Rozhraní
"""
>>> label.get_text()
'Pomeranč'
>>> label.get_color()
AttributeError: 'Label' object has no attribute 'get_color'
"""

# Vlastnost x
"""
>>> label.get_x()
0
>>> label.set_x(40)
<omw.Label object at 0x11065fe50>
>>> label.get_x()
40
"""

# Posun
"""
>>> label.move(10, 20)
<omw.Label object at 0x11065fe50>
"""

# Zřetězení
"""
>>> label.set_text("Rajče").move(-50, -20)
<omw.Label object at 0x11065fe50>
"""

# Instance třídy
"""
>>> label2 = Label()
>>> label2
<omw.Label object at 0x110490ad0>
>>> label
<omw.Label object at 0x11065fe50>
"""

# Okno
"""
>>> window2 = Window()
>>> label2.set_text("banán")
<omw.Label object at 0x110490ad0>
>>> window2.set_widget(label2)
<omw.Window object at 0x1106b3910>
"""

# window.main_loop()
