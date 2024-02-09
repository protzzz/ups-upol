# Ukládání a načítání dat
# Informujeme o případných chybách.
# Je potřeba vyřešit souběh při rychlém klikání na tlačítka.
from omw import *
import aio
storage = aio.Storage()
storage.set_max_delay(5)
storage.set_error_probability(0.8)

class Component(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        store_button = Button().set_text("Store").move(0, 30)
        load_button = Button().set_text("Load").move(100, 30)
        status_label = Label().move(0, 60)
        self.set_items([entry, store_button, load_button, status_label])

    def get_entry(self):
        return self.get_items()[0]

    def get_store_button(self):
        return self.get_items()[1]

    def get_load_button(self):
        return self.get_items()[2]

    def get_status_label(self):
        return self.get_items()[3]

    async def store_entry_text(self):
        text = self.get_entry().get_text()
        status_label = self.get_status_label()
        status_label.set_text("storing")
        try:
            await storage.set("text", text)
        except:
            status_label.set_text("storing error")
        else:
            status_label.set_text("stored")

    async def load_entry_text(self):
        status_label = self.get_status_label()
        status_label.set_text("loading")
        try:
            text = await storage.get("text")
        except:
            status_label.set_text("loading error")
        else:
            status_label.set_text("loaded")
            self.get_entry().set_text(text)
        
    def ev_button_clicked(self, sender, button):
        if button == self.get_store_button():
            aio.arun(self.store_entry_text())
        elif button == self.get_load_button():
            aio.arun(self.load_entry_text())
        
w = Window().set_widget(Component())
w.main_loop()
