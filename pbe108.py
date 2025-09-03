def add_name():
    file = open("names.txt", "a")
    name = str.capitalize(input("Type a new name to add: "))
    file.write(name)
    file.close()
    pass


def read_name():
    file = open("names.txt", "r")
    print(file.read())
    pass


add_name()
read_name()
