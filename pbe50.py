def low_or_high():
    while True:
        number = int(input("Enter a number between 10 and 20: "))
        if number < 10:
            print("to low")
            pass
        elif number > 20:
            print("to high")
            pass
        else:
            print("Thank you!")
            break
        pass
    pass


low_or_high()
