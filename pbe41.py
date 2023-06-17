def printer():
    name = str.capitalize(input("Enter your name: "))
    number = int(input("How many times do you want to print it? "))
    if number <= 10:
        for i in range(number):
            print(name)
            pass
    else:
        for i in range(3):
            print("Too high ")
            pass
        pass

    pass

printer()
