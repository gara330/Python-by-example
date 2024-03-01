def adder(number, total):
    total = total + number
    return total
    pass


def ask_number():
    total = 0
    for i in range(5):
        number = int(input("Enter a number: "))
        add_or_not = str.lower(input("Do you want to append it to the total? "))
        if add_or_not == "yes" or add_or_not == "y":
            total = adder(number, total)
            pass
        else:
            pass
        pass
    print("The total is: ", total)
    pass


ask_number()
