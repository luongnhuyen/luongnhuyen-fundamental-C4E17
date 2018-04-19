text = "champion"
characters = list(text)
loop = True
while loop:
    from random import choice    #chon ngau nhien ben trong 1 list
    c=0
    print(choice(characters),end=" ")
    if c == choice(characters):
        characters.remove(c)
    #
    if characters == 0:
        loop = False
