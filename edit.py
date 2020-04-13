import time
from menu import menu
import csv  
from newcontact import * 
import sys


class edit():
    def __init__(self):
        self.firstname = input('Search by First Name: ').capitalize().strip()
        
        csv_file = csv.reader(open('memory.csv', "r"), delimiter=",")
        for row in csv_file:
            if self.firstname == row[0]:
                print (row)
            else:
                
                pass
        time.sleep(3)
        menu()