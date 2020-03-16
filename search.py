import time
from menu import menu
import csv  
from newcontact import * 
import sys


class search():
    def __init__(self):
        #input number you want to search
        self.firstname = input('Enter First Name: ').capitalize().strip()
        
       #csv_file = csv.reader(open('memory.csv', "rb"), delimiter=",")
        
        with open('memory.csv', 'r') as f:
           reader = csv.reader(f)
           lines = list(reader)
           for row in reader:
                if self.firstname == input:
                    print (lines)[1]
                elif self.firstname == row[2]:
                    print(" ".join(row[2]))
                elif self.firstname == row[3]:
                    print(" ".join(self))
                
                else:
                    print('Name Not in Phonebook')
                    search()
        
        time.sleep(3)
        menu()