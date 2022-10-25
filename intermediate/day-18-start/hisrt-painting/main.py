# import colorgram
#
#
# def extract_colors(colors_object):
#     color_list = []
#     # print(len(colors_object))
#     for i in range(0, len(colors_object)):
#
#         f_color = colors_object[i]
#         r = f_color.rgb.r
#         g = f_color.rgb.g
#         b = f_color.rgb.b
#
#         color_list.append((r, g, b))
#     return color_list
#
#
#
# colors = colorgram.extract('image.jpeg', 40)
# hisrt_color_list = extract_colors(colors)
# print(hisrt_color_list)
import turtle as t
import random

screen = t.Screen()
tur = t.Turtle()

screen.colormode(255)
# tur.pencolor((220, 76, 48))

tur.speed(0)
color_list = [(244, 235, 46), (196, 12, 34), (170, 175, 240), (252, 6, 60), (5, 245, 224),
              (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26),
              (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28),
              (227, 161, 9), (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 215),
              (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238), (100, 226, 236), (243, 164, 155)]

tur.penup()
tur.hideturtle()
x = -250
y = -250
for _ in range(10):
    tur.goto(x, y)
    # print(tur.position())
    for _ in range(10):
        rand_1 = random.choice(color_list)
        tur.pendown()
        tur.dot(20, rand_1)
        tur.penup()
        tur.forward(50)
    y += 50
    # print(tur.position())

screen.exitonclick()
