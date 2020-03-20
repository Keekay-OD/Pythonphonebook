import time
from menu import menu
import csv  
from newcontact import * 
import sys


class search():
    def __init__(self):
        #input number you want to search
        self.firstname = input('Enter First Name: ').capitalize().strip()
        
        csv_file = csv.reader(open('memory.csv', "r"), delimiter=",")
        for row in csv_file:
            if self.firstname == row[0]:
                print (row)
            else:
                
                pass
        time.sleep(3)
        menu()