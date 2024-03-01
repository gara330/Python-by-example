import random


def random_colors():
    colors = ["red", "green", "blue", "white", "pink"]
    ran_color = random.choice(colors)
    while True:
        answer = str.lower(input("Enter a color: "))
        if answer == ran_color:
            print("Well done!")
            break
            pass
        else:
            if ran_color == "red":
                print("I bet you are red in anger")
                pass
            elif ran_color == "green":
                print("I bet you are green with envy")
                pass
            elif ran_color == "blue":
                print("You are probably feeling blue right now")
                pass
            elif ran_color == "white":
                print("Are you white as a sheet, as you diidn't guess correctly?")
                pass
            elif random == "pink":
                print("Shame you are not feeleing in th pink, as you got it wrong!")
                pass
            pass
        pass
    pass


random_colors()
