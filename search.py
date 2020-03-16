import pickle
import time
from menu import menu
import csv  
from newcontact import * 
class search():
    def __init__(self):
        
        self.firstname = input('Enter First Name: ').capitalize().strip()
        
        
        
        csv_file = "memory.csv"
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in address_book:
                    writer.writerow(data)

        
        time.sleep(3)


        
        menu()