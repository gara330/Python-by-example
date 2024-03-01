def ask_for_slices():
    initial_slices = int(input("How many slices do you start with? \n"))
    eaten_slices = int(input("How many slives have you eaten? \n"))
    if initial_slices > eaten_slices:
        slices_left = initial_slices - eaten_slices
        print("You still have ", slices_left, "left, queep going \n")
        pass
    else:
        print("That's impossible dude, try latter")
    pass


def main():
    ask_for_slices()
    pass


main()
