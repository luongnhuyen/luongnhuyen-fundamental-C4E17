# menu= ["pho", "com rang", "my xao","bun rieu"]
# print(menu)
#
# menu.append("hu tieu")
# print("After append")
# print(menu)
#
# # fori
# for i in range (len(menu)):
#     print(menu[i])
#
# # foreach
# for item in menu:
#     print(item)
#
# # for enum
# for i, item in enumerate(menu):
#     message = "{0}. {1}".format(i+1,item)
#     print(message)


name = "Nguyen"
age = 22
status = "Doc than"
address = "Doi Can"

message='''{0}
{1} tuoi
tinh trang quan he {2}
song o {3}'''.format(name, age, status, address)
print (message)
# print(name + ", " + str(age) + ", " + status "tuoi, " + address)
