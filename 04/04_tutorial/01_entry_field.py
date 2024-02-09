from omw import *

class EntryField(Group):
    def __init__(self):
        super().__init__()
        label = Label()
        entry = Entry().move(0, 20)
        self.set_items([label, entry])

    # Přidat metody get_label a get_entry
    def get_label(self):
        return self.get_items()[0]

    def get_entry(self):
        return self.get_items()[1]
    
    # Přidat vlastnost text (nastavuje vlastnost text entry)

    def get_text(self):
        return self.get_entry().get_text()

    def set_text(self, text):
        self.get_entry().set_text(text)
        return self
    
    # Přidat vlastnost label_text
    # Přidat vlastnosti x a y

ef = EntryField()
ef.get_label().set_text("Jméno:")
# ef.get_entry().set_text("ABC")
ef.set_text("ABC")
ef.move(20, 30)
w = Window().set_widget(ef)
