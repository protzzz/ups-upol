# Po stisku tlačítka okno nezamrzne
from omw import *
import aio

class Component(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        button = Button().set_text("Start").move(0, 30)
        label = Label().move(0, 60)
        self.set_items([entry, button, label])

    def get_label(self):
        return self.get_items()[2]

    async def compute(self):
        await aio.sleep(2)
        self.get_label().set_text("done")

    def ev_button_clicked(self, sender, origin):
        aio.arun(self.compute())
        
w = Window().set_widget(Component())
w.main_loop()
