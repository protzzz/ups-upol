from omw import *

class NameEntryGroup(Group):
    def __init__(self):
        super().__init__()
        label1 = Label().move(5, 5).set_text("Name:")
        entry1 = Entry().move(60, 0).set_text("Your name...")
        label2 = Label().move(60, 28)
        self.set_items([label1, entry1, label2])

    def get_name(self):
        return self.get_items()[1]
    
    def get_validate_name(self):
        return self.get_items()[2]
    
    def ev_change(self, sender):
        super().ev_change(sender)

        if sender == self.get_name():
            name = self.get_name().get_text()
            if not name:
                self.get_validate_name().set_text("Please enter your name.")
            else:
                self.get_validate_name().set_text("Your name was entered!")

class PasswordGroup(Group):
    def __init__(self):
        super().__init__()
        label1 = Label().set_text("Password:").move(5, 50)
        entry1 = Entry().move(60, 75).set_text("Write your password...")
        label2 = Label().move(60, 100).set_text("")
        entry2 = Entry().move(60, 130).set_text("Retype your password...")
        label3 = Label().move(60, 155).set_text("")
        self.set_items([label1, entry1, label2, entry2, label3])

    def get_password(self):
        return self.get_items()[1]

    def get_validate_password(self):
        return self.get_items()[2]

    def get_retyped_password(self):
        return self.get_items()[3]
    
    def get_validate_orginal_and_retyped_passwords(self):
        return self.get_items()[4]

    def validate_password(self):
        password = self.get_password().get_text()

        if not password:
            self.get_validate_password().set_text("Please enter a password.")
        elif len(password) < 8:
            self.get_validate_password().set_text("Password should be at least 8 characters long.")
        else:
            password_strength = 0
            description = ""

            if len(password) >= 8:
                password_strength += 1
            if any(c.isupper() for c in password):
                password_strength += 1
            if any(c.islower() for c in password):
                password_strength += 1
            if any(c.isdigit() for c in password):
                password_strength += 1
            if any(not c.isalnum() for c in password):
                password_strength += 1

            if password_strength == 0:
                description = "Verify process: Very Weak"
            elif password_strength == 1:
                description = "Verify process: Weak"
            elif password_strength == 2:
                description = "Verify process: Moderate"
            elif password_strength == 3:
                description = "Verify process: Strong"
            elif password_strength >= 4:
                description = "Verify process: Very Strong"

            self.get_validate_password().set_text(description)

    def validate_retyped_password(self):
        retyped_password = self.get_retyped_password().get_text()
        original_password = self.get_password().get_text()

        if not retyped_password:
            self.get_validate_orginal_and_retyped_passwords().set_text("Please retype your password.")
        elif original_password != retyped_password:
            self.get_validate_orginal_and_retyped_passwords().set_text("Passwords do not match.")
        else:
            self.get_validate_orginal_and_retyped_passwords().set_text("Passwords match.")

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_password():
            self.validate_password()
        elif sender == self.get_retyped_password():
            self.validate_retyped_password()

class ButtonGroup(Group):
    def __init__(self, name_group, password_group):
        super().__init__()
        self.name_group = name_group
        self.password_group = password_group
        button = Button().set_text("SIGN IN!").move(80, 180)
        label = Label().set_text("").move(60, 210)
        self.set_items([button, label])

    def get_status_of_registration(self):
        return self.get_items()[1]

    def create_user(self):
        name = self.name_group.get_name().get_text()
        password = self.password_group.get_password().get_text()
        retyped_password = self.password_group.get_retyped_password().get_text()

        if not name or not password or not retyped_password:
            self.get_status_of_registration().set_text("Please fill in all fields.")
        elif len(password) < 8:
            self.get_status_of_registration().set_text("Password should be at least 8 characters long.")
        elif password != retyped_password:
            self.get_status_of_registration().set_text("Passwords do not match.")
        else:
            self.get_status_of_registration().set_text("Registration successful.")

    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        self.create_user()

window = Window()

name = NameEntryGroup()
password = PasswordGroup()
button = ButtonGroup(name, password)

group = Group().set_items([name, password, button])

window.set_widget(group)
window.main_loop()