print("Welcome to our shop, what do you want?")
print("Our items:")
items = ["T-Shirt", "Sweater"]
print(*items, sep=', ')

new_item=input("Enter new item:")
items.append(new_item)
print(*items, sep=', ')

n= int(input("Update position:"))
items.pop(n-1)
m=input("New item?")
items.insert(n-1,m)
print(*items, sep=', ')

l=int(input("Delete position:"))
del(items[l])
print(*items, sep=', ')
