class new():
    def __init__(self):
        address_book = []

        self.firstname = input('Enter First Name: ').capitalize().strip()
        self.lastname = input('Enter Last Name: ').capitalize().strip()
        self.phone = input('Enter Phone #: ').strip()
        self.email = input('Enter Email: ').strip().lower()
        address_book.append({'name' : self.firstname, 'phone' : self.phone, 'adress' : self.email})
        print(self.firstname,self.lastname, 'Saved Succesfully')
        
        
    
