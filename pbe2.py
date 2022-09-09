def askFirstName():
    fName = input("What's your first name? \n")
    return fName

def askLasName():
    Lname = input("What's you last name? \n")
    return Lname

def sayHello(fName , lName):
    print("Hello" , fName , lName)
    pass

def main():
    fName = askFirstName()
    lName = askLasName()
    sayHello(fName , lName)

main()