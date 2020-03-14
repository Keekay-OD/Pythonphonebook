import pickle
import time
import csv  
from menu import menu
from search import search 
class new():
    def __init__(self):
        address_book = []
        self.firstname = input('Enter First Name: ').capitalize().strip()
        self.lastname = input('Enter Last Name: ').capitalize().strip()
        self.phone = input('Enter Phone #: ').strip()
        self.email = input('Enter Email: ').strip().lower()
        address_book.append({'name' : self.firstname, 'phone' : self.phone, 'adress' : self.email})
        

        with open('memory.csv', 'w') as f:
            for key in address_book.keys():
                f.write("%s,%s\n"%(key,address_book[key]))
       
       
       # with open('memory.csv', newline='') as address_book:
         #   w = csv.writer(open("memory.csv", "w"))

        print('Saving......')
        time.sleep(1)
        print('............')
        time.sleep(1)
        print(self.firstname,self.lastname, 'Saved Succesfully')
            

        
        time.sleep(3)


        
        menu()

        


    
