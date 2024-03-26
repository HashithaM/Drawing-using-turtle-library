import random
from turtle import Turtle
from random_color import Color
color = Color()
tim = Turtle()
tim.pensize(10)
tim.speed(0.1)


class RandomWalk:
    def __init__(self, iteration):
        self.iteration = iteration
        self.length = 25
        self.direction = [0, 90, 180, 270]
        self.colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
                  "SeaGreen"]

    def drawing(self):
        n = 0
        while n < self.iteration:
            new_color = color.generate_color()
            tim.color(new_color)
            tim.setheading(random.choice(self.direction))
            tim.forward(self.length)
            n += 1
