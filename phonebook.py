from getname import * 
from contact import *
from database import Contact
from search import search
import csv  
import time
from newcontact import new

#Checks User Name
getname()

def welcome():
    print("1. Add a new Contact")
    print('2. Search Contact')
    print('3. Remove Contact')
    print('4. Edit Contact')
    print('5. Exit')

    while True:
        try:
            choice = int(input('Enter [1-5] :'))
            break
        except ValueError:
            print("Please enter a vaild number!")
    if choice == 1:
        new()
    elif choice == 5 :
        time.sleep(1)
        print('You\'ve been successfully logged out')
        exit()
    elif choice == 2 :
        time.sleep(1)
        search() 
        
    elif choice == 4 :
        time.sleep(1)
        print ('Features Locked: Please Wait for update')

        
        
           
    else :
        time.sleep(1)
        print ('Features Locked: Please Wait for update')
    welcome()




        
        
        
    



if __name__ == '__main__': welcome()