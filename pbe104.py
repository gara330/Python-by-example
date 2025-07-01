def data_collect():
    data_set = {}
    for i in range(0, 2):
        name = str.capitalize(input("Enter a name: "))
        age = int(input("Enter the age: "))
        shoe = int(input("Enter the shoe size: "))
        data_set[name] = {"age": age, "Shoe size": shoe}
        pass
    getrid = str.capitalize(input("Which name do you want to delete? "))
    del data_set[getrid]
    for i in data_set:
        print((name), data_set[name])
    pass


data_collect()
