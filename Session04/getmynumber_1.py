loop = True
m = 50
a= str("Too small")
b= str("Too large")
c= str("Right")
while loop:
    n = input("Is {0} your number:".format(m))
    if n == a:
        m = m//2
        # print ("Is", m, "your number: ")
    if n == b:
        m=(m+m/2)//2
        # print ("Is", l, "your number: ")
    if n == c:
        print ("right")
    loop == c
