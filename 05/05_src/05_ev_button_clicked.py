# Skupina tlačítek
from omw import *

class Buttons(Group):
    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        print("Kliknuto na tlačítko:", sender.get_text())
    

window = Window()
button1 = Button().set_text("A")
button2 = Button().set_text("B").move(0, 30)
buttons = Buttons().set_items([button1, button2])
window.set_widget(buttons)
window.main_loop()