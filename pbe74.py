def colours_list():
    colours = [
        "red",
        "green",
        "blue",
        "pink",
        "cyan",
        "purple",
        "black",
        "white",
        "grey",
        "yellow",
    ]
    initial = int(input("Enter an initial number between 0 and 4: "))
    end = int(input("Enter a end number between 5 and 9: "))
    for i in range(initial, end + 1):
        print(colours[i])
        pass
    pass


colours_list()
