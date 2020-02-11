from newcontact import new
from welcome import welcome 


welcome()



print("1. Add a new Contact")
print('2. Search Contact')
print('3. Remove Contact')
print('4. Edit Contact')

choice = input('Enter [1-4] :')

choice = int(choice)

if choice == 1:
    new()
    
else :
    print ('Features Locked: Please Wait for update')

welcome ()