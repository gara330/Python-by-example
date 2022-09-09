def askName():
    fName = input("What's your first name? \n")
    lenName = len(fName)
    if lenName < 5:
        lName = input("And your last name? \n")
        fullName = str.upper(fName + lName)
        return fullName
        pass
    else:
        fName = str.lower(fName)
        return fName
        pass
    pass

def printName():
    name = askName()
    print(name)
    pass

printName()