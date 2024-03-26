import random
from extract_colors import color_list
from turtle import Turtle
tim = Turtle()


class HirstPainting:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        tim.penup()
        tim.setheading(225)
        tim.forward(300)
        tim.setheading(0)
        tim.pendown()
        for j in range(0, self.y):
            for i in range(0, self.x):
                tim.dot(20, random.choice(color_list))
                tim.penup()
                tim.forward(50)
                tim.pendown()
                print(f"{i}, {j}")
            tim.penup()
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)
            tim.pendown()

