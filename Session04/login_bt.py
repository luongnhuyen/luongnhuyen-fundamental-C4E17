wrong_count=0
loop= True

while loop:
    username = input ("Username?")
    password = input ("Password?")
    if username != 'c4e':
        print("No such user")
        wrong_count +=1
    elif password != 'codethechange':
        print("Wrong password")
        wrong_count +=1
    else:
        print("Welcome")
        loop = False
    if wrong_count > 3:
        loop = False
