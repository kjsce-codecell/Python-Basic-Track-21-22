d = {"Manasi": "1234",
  "Hussain": "0000",
  "Sahil": "6789",
  "Soumen": "0202"}
print("Enter username and password") 
while(True):
    username=input("Enter username: ") 
    if username in d.keys():
        print("Welcome " + username + "!") 
        # while(True):
        password=input("Enter password: ") 
        if(d[username]==password):
            print("Valid password")
            print("You have been logged in!\n") 
        else:
            print("Wrong password!\nRe-enter password.")
    else:
        print("Username does not exist") 
