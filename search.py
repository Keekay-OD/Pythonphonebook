import pickle
import time
from menu import menu
import csv  
class search():
    def __init__(self):
        address_book = []
        #w = csv.writer(open("memory.csv", "w"))
        self.firstname = input('Enter First Name: ').capitalize().strip()
        self.lastname = input('Enter Last Name: ').capitalize().strip()
        self.phone = input('Enter Phone #: ').strip()
        self.email = input('Enter Email: ').strip().lower()
        address_book.append({'name' : self.firstname, 'phone' : self.phone, 'adress' : self.email})
        

        with open('memory.csv', 'w') as csvfile:
            address_book = csv.reader(csvfile, delimiter='', quotechar='|')

        
        time.sleep(3)


        
        menu()