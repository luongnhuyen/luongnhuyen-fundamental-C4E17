prices={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock={
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
fruits = list(prices.keys())
for i in fruits:
    print(i)
    i ==prices.get(i,0)
    i ==stock.get(i,0)
    print("price: ",prices.get(i,0))
    print("stock: ",stock.get(i,0))
    print()

total = 0
total_fruits = 0
for i in fruits:
    i ==prices.get(i,0)
    i ==stock.get(i,0)
    total=prices.get(i,0)*stock.get(i,0)
    print("Total",i,": ", total)
    total_fruits = total_fruits + prices.get(i,0)*stock.get(i,0)

print("Total fruits: ",total_fruits)
