from random import choice
text = "champion"
characters = list(text)
for i in range(len(characters)):
    a=choice(characters)
    print(a,end=" ")
    characters.remove(a)
loop = True
while loop:
       #chon ngau nhien ben trong 1 list
    if len(characters) == 0:
        loop = False
