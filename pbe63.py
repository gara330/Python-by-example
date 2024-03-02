import turtle


scr = turtle.Screen()


def triangles():
    turtle.left(180)
    colors = ["red", "blue", "pink"]
    for i in range(0, 3):
        turtle.color(colors[i])
        turtle.begin_fill()
        for j in range(1, 4):
            turtle.forward(100)
            turtle.right(120)
            pass
        turtle.penup()
        turtle.left(180)
        turtle.forward(150)
        turtle.left(180)
        turtle.pendown()
        turtle.end_fill()
        pass
    turtle.exitonclick()
    pass


triangles()
