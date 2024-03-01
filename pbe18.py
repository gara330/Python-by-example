def ask_number():
    number = int(input("Enter a number: \n"))
    if number >= 10 and number <= 20:
        print("Correct!")
        pass
    elif number < 10:
        print("Too low")
        pass
    else:
        print("Too high")
        pass
    pass


ask_number()
