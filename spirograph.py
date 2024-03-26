from turtle import Turtle
from random_color import Color
tim = Turtle()
color = Color()
tim.speed(100)


class Spirograph:
    def __init__(self, radius, num_of_circles):
        self.radius = radius
        self.change_angle = 360/num_of_circles
        self.number_of_circles = num_of_circles
        self.i = 0
        self.angle = 0

    def draw(self):
        while self.i < self.number_of_circles:
            new_color = color.generate_color()
            tim.color(new_color)
            tim.circle(self.radius)
            print(self.angle)
            self.angle += self.change_angle
            tim.setheading(self.angle)
            print(self.i)
            self.i += 1

