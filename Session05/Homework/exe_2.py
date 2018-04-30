inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ['seashell', 'strange berry', 'lint']
print(inventory)

backpack= inventory["backpack"]
backpack.remove("dagger")
print(inventory)

gold=list(int(inventory["gold"]))
gold.append("50")
print(inventory)
