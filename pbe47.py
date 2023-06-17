def adder(number, total):
    total = total + number
    return total
    pass

def ask_for_number():
    total = 0
    number = int(input("Enter a number: "))
    total = adder(number, total)
    number2 = int(input("Enter a number to add: "))
    total = adder(number2, total)
    while True:
        answer = str.lower(input("Do you want to enter another number? y/n: "))
        if answer == "y" or answer == "yes":
            number = int(input("Enter another number: "))
            total = adder(number, total)
            pass
        else:
            break
            pass
        pass
    print(total)
    pass

ask_for_number()
