numbers= [1, 6, 8, 1, 2, 1, 5, 6]
n= int(input("Enter number: "))
count=0
i=0
while i < len(numbers):
    c=numbers[i]
    i+=1
    if n==c:
        count += 1
print(n, "appears", count, "times in my list")
