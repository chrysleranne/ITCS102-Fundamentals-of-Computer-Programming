from getpass import getpass

username = 'chryslrnnd' 
password = 'hatdog'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if(u == username) and (p == password) :
    print("Access Granted")

else:
    print("Access Denied")