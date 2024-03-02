import turtle

scr = turtle.Screen()


def number_1():
    turtle.left(90)
    turtle.forward(100)
    turtle.home()
    pass


def number_2():
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    turtle.home()
    pass


def number_3():
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    turtle.home()
    pass


number_1()
number_2()
number_3()

turtle.exitonclick()
