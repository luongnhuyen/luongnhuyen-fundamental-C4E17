print("Welcome to our shop, what do you want?")
print("Our items:")
items = ["T-Shirt", "Sweater"]
print(*items, sep=', ')

items.append("Jeans")
print(*items, sep=', ')

items.remove("Sweater")
items.insert(1,"Skirt")
print(*items, sep=', ')

del(items[2])
print(*items, sep=', ')
