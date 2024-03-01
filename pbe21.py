def ask_name():
    first_name = str.capitalize(input("What's your name? \n"))
    last_name = str.capitalize(input("And what's your last name? \n"))
    full_name = first_name + " " + last_name
    length = len(full_name)
    print(full_name)
    print(length)
    pass


ask_name()
