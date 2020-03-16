import pickle
import time
import csv  
from menu import menu



class new():
    def __init__(self):
        csv_columns = ['First Name','Last Name','Phone #','Email']
        address_book = []
        self.firstname = input('Enter First Name: ').capitalize().strip()
        self.lastname = input('Enter Last Name: ').capitalize().strip()
        self.phone = input('Enter Phone #: ').strip()
        self.email = input('Enter Email: ').strip().lower()
        address_book.append({'First Name' : self.firstname,'Last Name' : self.lastname, 'Phone #' : self.phone, 'Email' : self.email})
        
        csv_file = "memory.csv"
        print('Saving......')
        time.sleep(1)
        print('............')
        time.sleep(1)
        print(self.firstname,self.lastname, 'Saved Succesfully')
        time.sleep(3)
        
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in address_book:
                    writer.writerow(data)
            
        
        
            

        
        


        
        menu()

        


    
