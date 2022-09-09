def askName():
    fName = str.capitalize(input("What's your name? \n"))
    lName = str.capitalize(input("And what's your last name? \n"))
    fullName = fName + " " +lName
    length= len(fullName)
    print(fullName)
    print(length)
    pass

askName()