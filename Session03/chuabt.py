

n=int(input("Enter n:"))
m=int(input("Enter m:"))

for i in range (n):
    for j in range (m):
        print("* ", end="")
        print(i,j, sep=",", end="")
        print(", ", end="")
    print()
