import pickle
import time
from menu import menu
import csv  
from newcontact import * 
import sys


class search():
    def __init__(self):
        #input number you want to search
        self.firstname = input('Enter First Name: ').capitalize().strip()
        
        #read csv, and split on "," the line
        csv_file = csv.reader(open('memory.csv', "rU"), delimiter=",")
        header1 = csv_file.next()
        #loop through csv list

        query = dict(csv_file)
        for row in csv_file:
        
            if self.firstname == row[1]:
                print (row)
            else:
                print('Name Not in Phonebook')
                search()
        
        time.sleep(3)
        menu()