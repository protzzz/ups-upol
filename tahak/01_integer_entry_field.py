from omw import *
class IntegerEntry(Entry):
    def get_value(self):
        return int(self.get_text())

    def set_value(self, value):
        return self.set_text(str(value))
    
    def is_valid(self):
        return self.get_text().isdecimal()

class IntegerEntryField(Group):
    def __init__(self):
        super().__init__()
        label = Label()
        entry = IntegerEntry().move(0, 20)
        validation_label = Label().move(0, 50)
        self.set_items([label, entry, validation_label])

    def get_label(self):
        return self.get_items()[0]

    def get_entry(self):
        return self.get_items()[1]

    def get_validation_label(self):
        return self.get_items()[2]

    def validate(self):
        if self.get_entry().is_valid():
            text = ""
        else:
            text = "Není číslo"
        self.get_validation_label().set_text(text)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_entry():
            self.validate()
            
    
e = IntegerEntryField()
e.get_label().set_text("Zadej věk:")
w = Window().set_widget(e)
w.main_loop()