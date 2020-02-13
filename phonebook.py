from newcontact import new
from welcome import welcome as menu
from getname import * 
from contact import *
from database import Contact



getname()
menu()

print('What can i do for you today', name,'? ')


def welcome():
    print("1. Add a new Contact")
    print('2. Search Contact')
    print('3. Remove Contact')
    print('4. Edit Contact')
    print('5. Exit')

    
    while True:
        try:
            choice = int(input('Enter [1-4] :'))
            break
        except ValueError:
            print("Please enter a vaild number!")
    if choice == 1:
        new()
        menu()
        welcome()
        
        
    elif choice == 5 :
        print('You\'ve been successfully logged out')
        exit()
    else :
        print ('Features Locked: Please Wait for update')
    



if __name__ == '__main__': welcome()