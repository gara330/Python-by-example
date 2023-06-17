def adder(number, total):
    total = total + number 
    return total
    pass

def ask_for_number():
    total = 0
    while total <= 50:
        number = int(input("Enter a number: "))
        total = adder(number, total)
        print("the total is: ", total)
        pass
    print("The final total is: ", total)
    pass

ask_for_number()
