# Zpráva button_clicked se zašle tlačítku poté,
# co na něj uživatel klikl.
from omw import *

class PrintButton(Button):
    def button_clicked(self):
        super().button_clicked()
        print("Kliknuto na tlačítko")
    

window = Window()
button = PrintButton().set_text("Klikni na mě!")
window.set_widget(button)

window.main_loop()