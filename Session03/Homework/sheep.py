print("Hello, my name is Yen and there are my ship sizes")
sizes=[5, 7, 300, 90, 24, 50, 75]
print(sizes)

a=max(sizes)
print("Now my biggest has size", a, "let's shear it")

sizes[sizes.index(a)] = 8
print("After shearing, here is my flock")
print(sizes)

for i in range (7):
    sizes[sizes.index(sizes[i])]=sizes[i]+50
print("One month has passed, now is my flock",sizes)
