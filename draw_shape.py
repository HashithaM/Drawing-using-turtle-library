from turtle import Turtle
tim = Turtle()
tim.color("blue")


class DrawShape:
    def __init__(self, no_sides, colors):
        self.sides = no_sides
        self.color = colors

    def draw(self):
        for _ in range(self.sides):
            tim.color(self.color)
            tim.forward(100)
            tim.left(360 / self.sides)
