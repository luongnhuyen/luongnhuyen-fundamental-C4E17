from random import *
n= randint(0,100)
wrong_count = 0
loop = True
while loop:
    m= int(input("Get my number?: "))
    if m == n:
        print("Bingo")
    elif m < n:
        print("Too small")
        wrong_count += 1
    else:
        print("Too large")
        wrong_count += 1
    loop = m
    if wrong_count >= 5:
        loop = False
        print ("Gameover")
