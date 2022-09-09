def askNumber():
    number = int(input("Enter a number below 20: \n"))
    if number >= 20:
        print("Too high, try again")
    else:
        print("Thank you!")
        pass
    pass

askNumber()