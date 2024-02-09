# Palindrom entry
from omw import *

class PalindromEntry(Group):
    def __init__(self):
        super().__init__()
        entry = Entry()
        label = Label().move(0, 30)
        self.set_items([entry, label])
        self.ensure_label_text()

    def get_entry(self):
        return self.get_items()[0]

    def get_label(self):
        return self.get_items()[1]

    def is_palindrom(self):
        text = self.get_entry().get_text()
        return text == text[::-1]

    def ensure_label_text(self):
        if self.is_palindrom():
            text = "Je palindrom"
        else:
            text = "Není palindrom"
        label = self.get_label()
        label.set_text(text)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_entry():
            self.ensure_label_text()
    

window = Window()
entry = PalindromEntry()
window.set_widget(entry)
window.main_loop()