from omw import *
class IntegerEntry(Entry):
    # přidat vlastnost value (číselná hodnota)

    def get_value(self):
        return int(self.get_text())

    def set_value(self, value):
        return self.set_text(str(value))

    # přidat metodu is_valid()
    
    def is_valid(self):
        return self.get_text().isdecimal()
        
    
e = IntegerEntry()
w = Window().set_widget(e)

# Úkol: napsat třídu IntegerEntryField
# Instance jsou pole na zadávání čísel,
# kde nad polem je popisek a pod polem
# validační hlášení.
#
# Validační hlášení se aktualizuje zasláním
# zprávy validate bez argumentů.
