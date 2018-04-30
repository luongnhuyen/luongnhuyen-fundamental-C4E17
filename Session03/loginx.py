from getpass import getpass

while True:

    user=input("Your user:")
    password=getpass("Your password: ")
    if user == "C4E":
        if password == "codethechange":
            print ("Welcome")
        else:
            print("Wrong password")
    else:
        print("Wrong user")
        break
