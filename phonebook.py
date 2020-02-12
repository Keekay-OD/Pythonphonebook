from newcontact import new
from welcome import welcome 
from getname import * 

getname()



print('What can i do for you today', name,'? ')


while welcome():
    print("1. Add a new Contact")
    print('2. Search Contact')
    print('3. Remove Contact')
    print('4. Edit Contact')

    
    while True:
        try:
            choice = int(input('Enter [1-4] :'))
            break
        except ValueError:
            print("Please enter a vaild number!")
    if choice == 1:
        new()
        break
    
    else :
        print ('Features Locked: Please Wait for update')
        

welcome ()