# Událost ev_change se zasílá po změně objektu.
from omw import *

class LoggingGroup(Group):
    def ev_change(self, sender):
        super().ev_change(sender)
        print("Změna prvku:", sender)
    

window = Window()
entry = Entry()
checkbox = Checkbox().move(0, 30)
group = LoggingGroup().set_items([entry, checkbox])
window.set_widget(group)

# Také vyvolá změnu:
"""
>>> checkbox.move(10, 0)
Změna prvku: <omw.Checkbox object at 0x1047fc450>
<omw.Checkbox object at 0x1047fc450>
"""

window.main_loop()