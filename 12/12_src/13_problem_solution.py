# Dlouhý výpočet spuštěn v samostatném procesu.
from omw import *
from co import *
import time
import aio

stop_flag = True
process = None

def run_computation():
    global stop_flag
    time.sleep(5) # Dlouhý výpočet
    stop_flag = True
        
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
                   
    async def update_status(self):
        while True:
            await aio.sleep(0.01)
            if stop_flag:
                self.get_progress_label().set_text("done")
                return None

    def start_computation(self):
        global process
        global stop_flag
        stop_flag = False
        process = start_process(run_computation)
        self.get_progress_label().set_text("computing")
        aio.arun(self.update_status())
        

    def ev_button_clicked(self, sender, button):
        if button == self.get_start_button():
            if stop_flag:
                self.start_computation()
            
        
c = Component()
w = Window().set_widget(c)
w.main_loop()
if process != None:
    join_process(process)

