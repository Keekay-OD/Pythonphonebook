class Contact:

    def __init__(self, firstname, lastname, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email

    def edit_name(self, firstname):
        self.firstname = firstname
        return self.firstname

    def edit_lastname(self, lastname):
        self.lastname = lastname
        return self.lastname

    def edit_phone(self, phone):
        self.phone = phone
        return self.phone

    def edit_email(self, email):
        self.email = email
        return self.email

    @classmethod
    def add(cls, name, surname, number, email):
        return cls(firstname, lastname, phone, email)