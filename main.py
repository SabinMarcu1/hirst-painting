"""import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
   r = color.rgb.r
   g = color.rgb.g
   b = color.rgb.b
   new_color = (r, g, b)
   rgb_colors.append(new_color)"""
# import turtle
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
color_list = [(235, 226, 207), (216, 217, 223), (206, 157, 107), (107, 109, 128), (141, 141, 154), (236, 214, 225),
              (223, 211, 116), (175, 73, 37), (203, 148, 174), (219, 233, 222), (178, 157, 43), (106, 112, 168),
              (187, 15, 4), (16, 18, 59), (16, 33, 17), (226, 169, 195), (33, 32, 15), (213, 83, 60), (233, 173, 161),
              (192, 10, 19), (42, 45, 114), (154, 168, 157), (140, 77, 88), (89, 104, 93), (181, 181, 218),
              (202, 79, 92), (33, 17, 32), (223, 210, 20), (72, 76, 40), (179, 200, 182)]

tim.setheading(225)
tim.penup()
tim.forward(350)
tim.setheading(0)

num_rows = 10

for row in range(num_rows):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
