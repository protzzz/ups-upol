# Okno hlásící kliknutí na libovolné tlačítko, které obsahuje.
from omw import *

class ButtonsWindow(Window):
    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        print("Odesílatel:", sender)
        print("Kliknuto na tlačítko:", button.get_text())
    

window = ButtonsWindow()
button1 = Button().set_text("A")
button2 = Button().set_text("B").move(0, 30)
buttons = Group().set_items([button1, button2])
window.set_widget(buttons)
window.main_loop()