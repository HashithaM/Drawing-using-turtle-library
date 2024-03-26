from turtle import Turtle, Screen
import random
from random_walk import RandomWalk
from draw_shape import DrawShape
from spirograph import Spirograph
from hirst_painting import HirstPainting

tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

for _ in range(50):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

no_sides = 3
side_limit = 10
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
while no_sides < side_limit:
    shape = DrawShape(no_sides, random.choice(colors))
    shape.draw()
    no_sides += 1
    print(no_sides)

iteration = 200
random_walk = RandomWalk(iteration)
random_walk.drawing()

radius = 100
num_of_circles = 180
spirograph = Spirograph(radius, num_of_circles)
spirograph.draw()

x = 10
y = 10
hirst_painting = HirstPainting(x, y)
hirst_painting.draw()

screen = Screen()
screen.exitonclick()
