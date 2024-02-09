# Hodiny
# Spouštění korutiny před zobrazením okna.
# Textové pole zde máme pro kontrolu, že okno nezamrzlo.

from omw import *
import aio
import time

def get_current_time():
    return time.strftime("%H:%M:%S", time.gmtime())

class Clock(Label):
    async def update(self):
        while True:
            self.set_text(get_current_time())
            await aio.sleep(1)

clock = Clock()
entry = Entry().move(0, 30)
group = Group().set_items([clock, entry])
window = Window().set_widget(group)
window.main_loop(clock.update())
