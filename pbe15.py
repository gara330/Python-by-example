from tkinter.colorchooser import askcolor


def askColor():
    color = str.capitalize(input("What's your favorite color? \n"))
    if color == "Red":
        print("I like Red too!")
        pass
    else:
        print("I don't like", color, "I prefer Red")
        pass
    pass

askColor()