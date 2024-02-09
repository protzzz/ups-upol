from omw import *
import aio
import time


storage = aio.Storage()
storage.set_max_delay(3)

class Clock(Label):
    async def update(self):
        while True:
            self.set_text(get_current_time())
            await aio.sleep(1)

def get_current_time():
    return time.strftime("%H:%M:%S", time.gmtime())

class Component(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        add_button = Button().set_text("ADD").move(150, 0)
        label = Label().move(60,30)
        proccess_status = Label().move(0, 30)
        self.set_items([entry, add_button, label, proccess_status])
        self.string = ""
        self.index = 0

    def get_entry(self):
        return self.get_items()[0]

    def get_add_button(self):
        return self.get_items()[1]

    def get_task_label(self):
        return self.get_items()[2]

    def get_status_label(self):
        return self.get_items()[3]
    
    def create_index(self):
        return self.index + 1

    def new_string(self, text):
        return self.string + text + '\n'
    
    async def add_to_storage(self):
        word =  self.get_entry().get_text()
        if word:
            index = self.create_index()
            process_status = self.get_status_label()
            process_status.set_text("Loading...")
            await storage.set(index, word)
            text = await storage.get(index)
            self.index = index
            added_time = get_current_time()
            process_status.set_text(f"{text} was added at {added_time}")
            self.string = self.new_string(text)
            self.get_task_label().set_text(self.string)
            self.get_entry().set_text("")

    def ev_button_clicked(self, sender, button):
            if button == self.get_add_button():
                aio.arun(self.add_to_storage())

clock = Clock()
window = Window().set_widget(Component())
window.main_loop(clock.update())