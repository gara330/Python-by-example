def ask_name():
    first_name = input("What's your first name? \n")
    len_name = len(first_name)
    if len_name < 5:
        l_name = input("And your last name? \n")
        full_name = str.upper(first_name + l_name)
        return full_name
        pass
    else:
        first_name = str.lower(first_name)
        return first_name
        pass
    pass


def printName():
    name = ask_name()
    print(name)
    pass


printName()
