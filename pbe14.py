def askNumber():
    number = int(input("Enter a number between 10 and 20: \n"))
    if number >= 10 and number <= 20:
        print("Thank you!")
        pass
    else:
        print("incorrect")
        pass
    pass

askNumber()