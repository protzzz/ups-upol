# Okno hlásící každou změnu svého obsahu.
from omw import *

class LoggingWindow(Window):
    def ev_change(self, sender):
        super().ev_change(sender)
        print("Změna obsahu okna")
    

window = LoggingWindow()
entry = Entry()
checkbox = Checkbox().move(0, 30)
group = Group().set_items([entry, checkbox])
window.set_widget(group)

window.main_loop()