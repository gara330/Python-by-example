import turtle


scr = turtle.Screen()


def mandala():
    for i in range(0, 8):
        turtle.forward(100)
        turtle.right(45)
        pass
    turtle.right(36)
    pass


for i in range(0, 10):
    mandala()
    pass
turtle.exitonclick()
