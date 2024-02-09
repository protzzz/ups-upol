# Zaškrtávací pole a přepínač v omw verze 2
from omw import *

checkbox = Checkbox()
radiobutton = Radiobutton().move(0, 20)

group = Group().set_items([checkbox, radiobutton]).move(10, 10)


window = Window().set_widget(group)


# posílání zpráv zaškrtávacímu poli
"""
>>> checkbox.set_value(True)
<omw.Checkbox object at 0x10da26dd0>
>>> checkbox.get_value()
True
>>> checkbox.is_selected()
True
>>> checkbox.toggle()
<omw.Checkbox object at 0x10da26dd0>
>>> checkbox.is_selected()
False
"""

# přepínač reaguje na zprávy podobně
