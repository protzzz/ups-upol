from omw import *
import aio
storage = aio.Storage()
storage.set_max_delay(1)

class Component(Group):
    def __init__(self):
        super().__init__()
        entry1 = Entry()
        entry2 = Entry().move(0, 30)
        swap_button = Button().set_text("Swap").move(0, 60)
        status_label = Label().move(0, 90)
        self.set_items([entry1, entry2, swap_button, status_label])

    def get_entry1(self):
        return self.get_items()[0]

    def get_entry2(self):
        return self.get_items()[1]

    def get_swap_button(self):
        return self.get_items()[2]

    def get_status_label(self):
        return self.get_items()[3]

    async def swap_entry_text(self):
        text1 = self.get_entry1().get_text()
        text2 = self.get_entry2().get_text()
        self.get_status_label().set_text("processing")
        await storage.set("text1", text2)
        await storage.set("text2", text1)
        text1 = await storage.get("text1")
        text2 = await storage.get("text2")
        self.get_status_label().set_text("")
        # print(text1, text2)
        self.get_entry1().set_text(text1)
        self.get_entry2().set_text(text2)

        
    def ev_button_clicked(self, sender, button):
        if button == self.get_swap_button():
            aio.arun(self.swap_entry_text())

c = Component()
w = Window().set_widget(c)
w.main_loop()
