import turtle
import random

scr = turtle.Screen()


def octagon():
    colors = ["red", "green", "blue", "pink", "black", "cyan"]
    turtle.pensize(3)
    for i in range(0, 8):
        outline = random.choice(colors)
        turtle.color(outline)
        turtle.forward(100)
        turtle.left(45)
        pass
    turtle.exitonclick()
    pass


octagon()
