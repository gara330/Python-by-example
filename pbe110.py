def read_file():
    names = open("names.txt", "r")
    print(names.read())
    names.close
    pass
def new_file():
    name = str.capitalize(input("Select a name from the list to not be included: "))
    names = open("names.txt", "r")
    for row in names:
        if row != name:
            file = open("names2.txt", "a")
            new_name = row
            file.write(new_name)
            file.close()
            pass
        pass
    file.close()
    pass


read_file()
new_file()
