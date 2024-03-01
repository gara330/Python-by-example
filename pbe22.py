def ask_name():
    first_name = input("What's your name? \n")
    last_name = input("What's you last name \n")
    full_name = str.title(first_name + " " + last_name)
    print(full_name)
    pass


ask_name()
