def square():
    number = int(input("Enter one of its sides: "))
    area = number**2
    print("The area is: ", area)
    pass

def triangle():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = base * height / 2
    print("The area is", area)
    pass

def menu():
    opt = int(input("1) Square \n2) Triangle \n \nEnter a number to select an option: "))
    if opt == 1:
        square()
        pass
    elif opt == 2:
        triangle ()
        pass
    else:
        print("Not a valid option!")
    pass

menu()
