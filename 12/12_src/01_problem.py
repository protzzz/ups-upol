# Problém s dlouhým výpočtem:
# Při kliku na tlačítko okno na pět vteřin zamrzne.
from omw import *
import time

def run_computation():
    time.sleep(5)

class Component(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        start_button = Button().set_text("Compute").move(0, 30)
        progress_label = Label().move(0, 60)
        self.set_items([entry, start_button, progress_label])

    def get_entry(self):
        return self.get_items()[0]

    def get_start_button(self):
        return self.get_items()[1]

    def get_progress_label(self):
        return self.get_items()[2]
                
    def run_computation(self):
        self.get_progress_label().set_text("computing")
        run_computation()
        self.get_progress_label().set_text("done")

    def ev_button_clicked(self, sender, button):
        if button == self.get_start_button():
            self.run_computation()
            
        
c = Component()
w = Window().set_widget(c)
w.main_loop()

