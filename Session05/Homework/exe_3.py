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
