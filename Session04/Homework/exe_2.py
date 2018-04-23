print('''Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' is my guess is 'C'orrect
's' is my guess is 'S'maller than your number
'l' is my guess is 'L'arger than your number''')

loop = True
m = 50
m1=0
m2=100

a= str("s")
b= str("l")
c= str("c")
while loop:
    n = input("Is {0} your number:".format(m))
    if n == a:
        m2 = m
        m = m1+(m2-m1)//2
        # print ("Is", m, "your number: ")
    elif n == b:
        m1 = m
        m = m1+(m2-m1)//2
        # print ("Is", l, "your number: ")
    elif n == c:
        print ("Correct")
    if m1==m2:
        loop = False
        print ("Wrong")

    loop == c
