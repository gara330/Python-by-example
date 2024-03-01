def counter():
    number = 0
    while number <= 5:
        last_number = number
        number = int(input("Enter a number if it is over 5 I stop: "))
        pass
    print("The last number you entered was: ", last_number)
    pass


counter()
