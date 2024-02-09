# Problém: při kliknutí na tlačítko okno zamrzne.
from omw import *
import time

class Component(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        button = Button().set_text("Start").move(0, 30)
        label = Label().move(0, 60)
        self.set_items([entry, button, label])

    def get_label(self):
        return self.get_items()[2]

    def ev_button_clicked(self, sender, origin):
        time.sleep(2) # Simulace činnosti
        self.get_label().set_text("done")

w = Window().set_widget(Component())
