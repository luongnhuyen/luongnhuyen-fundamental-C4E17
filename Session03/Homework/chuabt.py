from turtle import *

# color_list=["red", "blue", "brown", "yellow", "grey"]
# for n in range (3,8):
#     selected_color = color_list[n-3]
#     color(selected_color)
#     for i in range(n):
#         forward (100)
#         left(360/n)

color_list = ["red", "blue", "brown", "yellow", "grey"]
color_n = len(color_list)
for n in range (3,12):
    selected_color = color_list[(n-3) % color_n]
    color(selected_color)
    for i in range(n):
        forward (100)
        left(360/n)



mainloop()
