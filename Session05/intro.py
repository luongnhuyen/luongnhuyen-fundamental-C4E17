# person = ["Quan", 40, "single", "Ha Noi", 2, 11]

# person = {}
# print(person)

# person = {
#     "name": "Quan"
# }
# print(person)

person = {
    "name": "Quan",
    "age": 40,

}
#update
person["age"]=22
print(person)

#creat
person["Home"]="Ha Noi"

#delete
# del person["age"]
# print(person)


print(*person.keys())

print(*person.values())

for key, value in person.items():
    print(key,":", value)


# print(person)

# # print(person["age"])
# person["age"]=22
# print(person)
#
#
# if "home" in person:
#     print(person["home"])
# else:
#     print("'name' is not in person")
