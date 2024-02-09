# Skupiny ovládacích prvků

from omw import *

window = Window()
label = Label().set_text("Jméno:").move(20, 20)
entry = Entry().move(20, 40)
group = Group().set_items([label, entry])
window.set_widget(group)

# Posun prvků ve skupině
"""
>>> group.move(0, 40)
<omw.Group object at 0x108f40e10>
"""

window.main_loop()
