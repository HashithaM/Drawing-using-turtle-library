import random
import turtle as t
t.colormode(255)


class Color:

    @staticmethod
    def generate_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        return random_color
