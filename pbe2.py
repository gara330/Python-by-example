def ask_first_name():
    fName = input("What's your first name? \n")
    return fName


def ask_last_name():
    Lname = input("What's you last name? \n")
    return Lname


def say_hello(fName, lName):
    print("Hello", fName, lName)
    pass


def main():
    fName = ask_first_name()
    lName = ask_last_name()
    say_hello(fName, lName)


main()
