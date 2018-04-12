n=int(input("Nhap so"))
a=int(n%2)
if a == 1:
    for i in range(1,n,2):
        print("x *",end=' ')
    print("x")
else:
    for i in range(1,n,2):
        print("x *",end=' ')
