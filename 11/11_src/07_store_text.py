# Ukládání a načítání dat
# Uživatel neví, co se děje.
from omw import *
import aio
storage = aio.Storage()
storage.set_max_delay(5)

class Component(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        store_button = Button().set_text("Store").move(0, 30)
        load_button = Button().set_text("Load").move(100, 30)
        self.set_items([entry, store_button, load_button])

    def get_entry(self):
        return self.get_items()[0]

    def get_store_button(self):
        return self.get_items()[1]

    def get_load_button(self):
        return self.get_items()[2]

    async def store_entry_text(self):
        text = self.get_entry().get_text()
        await storage.set("text", text)

    async def load_entry_text(self):
        text = await storage.get("text")
        self.get_entry().set_text(text)
        
    def ev_button_clicked(self, sender, button):
        if button == self.get_store_button():
            aio.arun(self.store_entry_text())
        elif button == self.get_load_button():
            aio.arun(self.load_entry_text())
        
w = Window().set_widget(Component())
w.main_loop()
