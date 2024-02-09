# Zaslání vlastní události
from omw import *

class TextChangeEntry(Entry):
    def set_text(self, text):
        super().set_text(text)
        self.send_event("ev_text_change")
        return self

class LoggingGroup(Group):
    def ev_text_change(self, sender):
        print("Change of text of entry:", sender)
    

window = Window()
entry = TextChangeEntry()
group = LoggingGroup().set_items([entry])
window.set_widget(group)

# Nezašle událost ev_text_change:
"""
>>> entry.move(10, 0)
"""
# Zašle událost ev_text_change:
"""
>>> entry.set_text("ABC")
Change of text of entry: <__main__.TextChangeEntry object at 0x104264350>
"""
