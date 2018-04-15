# name1="canh"
# name2="hieu"
# name3="duc anh"
# name4="nguyen"
# name5="don"

# names = []
# print(names)
# print(type(names))

# names = ["Canh"]
# print(names)

names = ["Canh", "Hieu", "Duc Anh", "Don"]
# # print(names)
#
#
# names.append("Nguyen")
# print(names)
#
# new_name = "Don"
# names.append(new_name)
# print(names)
#
# n=input("Ten:")
# names.append(n)
# print(names)

# Favs= ["teaching","death note","netflix"]
# print("Hi, favs:")
# print(*favs, sep=', ')
#
# new_pav= input("Enter new fav:")
# favs.append(new_pav)
# print(*favs, sep=', ')

# print(names[-3])

# names[0]= "Canh dai ka"
# print(names)

# print(len(names))
#
# for i in range (len(names)):
#     print(names[i])

# for i in range(len(names)):
#     print(i+1,"\b.",names[i])

# no=1
# for n in names:
#     print(no,". ", n, sep="")
#     no +=1

no=1
for n in names:
    message = "{0}.{1}".format(no, n)
    print(message)
    no +=1
