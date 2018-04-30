# for i in range (1,10):
#     print()
#     for j in range (1,10):
#
#         if (i+j)%2==0:
#             print (1,"\t",end="")
#         else:
#             print (0,"\t",end="")


n=int(input("Enter a number: "))
for i in range (1,n):
    print()
    for j in range (1,n):

        if (i+j)%2==0:
            print (1,"\t",end="")
        else:
            print (0,"\t",end="")
