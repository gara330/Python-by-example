def name_len():
    first_name = input(str.capitalize("What's your first name: "))
    leng = len(first_name)
    print("Your names has ", leng, " letters")
    return (first_name, leng)
    pass


def lname_len():
    last_name = input(str.capitalize("What's you last name? "))
    leng = len(last_name)
    print("Your last name has ", leng, " letters")
    return (last_name, leng)
    pass


def full_name(first_name, last_name):
    f_name = first_name + " " + last_name
    print(f_name)
    print("your full name has ", len(f_name), " letters")

    pass


firts_name, first_len = name_len()
last_name, last_len = lname_len()
full_name(firts_name, last_name)
