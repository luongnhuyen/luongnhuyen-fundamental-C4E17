n=int(input("Enter n:"))

for i in range (n):
    for j in range (n):
        if i <= j:
            print("* ", end="")
    print()
