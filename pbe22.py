def askName():
    fName = input("What's your name? \n")
    lName = input("What's you last name \n")
    fullName = str.title(fName + " " + lName)
    print(fullName)
    pass

askName()