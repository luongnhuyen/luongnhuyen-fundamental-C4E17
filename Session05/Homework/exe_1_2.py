# px = 1
# py = 1
p = {
    "x": 1,
    "y": 1
}

# bx = 2
# by = 2

b = {
    "x": 2,
    "y": 2
}

boxes = [
    {
        "x": 2,
        "y": 2
    },
    {
        "x": 3,
        "y": 4
    }
]

# print(boxes[0]["x"])

# for box in boxes:
#     print(box["y"])

while True:
    for y in range(4):
        for x in range(4):
            if x == p["x"] and y == p["y"]:
                print("P ", end="")
            elif x == b["x"] and y == b["y"]:
                print("B ", end="")
            elif x == 1 and y == 3:
                print("G ", end="")
            else:
                print("- ", end="")
        print()

    move = input("Your move (W/A/S/D)? ").upper()

    next_px = p["x"]
    next_py = p["y"]

    dx = 0
    dy = 0

    # next_p = p + d

    if move == "D":
        dx = 1
    elif move == "A":
        dx = -1
    elif move == "S":
        dy = 1
    elif move == "W":
        dy = -1

    next_px += dx
    next_py += dy

    if next_px == b["x"] and next_py == b["y"]:
        b["x"] += dx
        b["y"] += dy

    if 0 <= next_px < 4:
        p["x"] = next_px

    if 0 <= next_py < 4:
        p["y"] = next_py

    if b["x"] == 1 and b["y"] == 3:
        print("Pass")
        break
