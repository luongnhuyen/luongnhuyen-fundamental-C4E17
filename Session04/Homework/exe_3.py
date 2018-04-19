text = "champion"
characters = list(text)
loop = True
while loop:
    from random import choice    #chon ngau nhien ben trong 1 list
    characters=characters
    print(choice(characters),end=" ")

    characters.remove(choice(characters))
    #
    if len(characters) == 0:
        loop = False
