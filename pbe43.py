def count_up(number):
    for i in range(1, number + 1):
        print(i)
    pass


def count_down(number):
    for i in range(20, number - 1, -1):
        print(i)
        pass
    pass


def menu():
    opt = str.lower(input("Do you want to count up or down? "))
    if opt == "down" or opt == "d":
        number = int(input("Enter a number below 20: "))
        count_down(number)
        pass
    elif opt == "up" or opt == "u":
        number = int(input("Enter a number: "))
        count_up(number)
        pass
    else:
        print("I don't understand")
        pass
    pass


menu()
