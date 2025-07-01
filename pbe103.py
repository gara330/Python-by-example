def data_collect():
    data_set = {}
    for i in range(0, 4):
        name = str.capitalize(input("Enter a name: "))
        age = int(input("Enter the age: "))
        shoe = int(input("Enter the shoe size: "))
        data_set[name] = {"age": age, "Shoe size": shoe}
        pass
    for i in data_set:
        print((name), data_set[name]["age"])
    pass


data_collect()
