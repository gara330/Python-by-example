import turtle
import random

scr = turtle.Screen()


def random_pattern():
    lines = int(random.randint(1, 20))
    for i in range(0, lines):
        deg = int(random.randint(1, 365))
        lengh = int(random.randint(25, 100))
        turtle.forward(lengh)
        turtle.left(deg)
        pass
    turtle.exitonclick()
    pass


random_pattern()
