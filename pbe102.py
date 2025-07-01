def data_collect():
    data_set = {}
    for i in range(0, 4):
        name = str.capitalize(input("Enter a name: "))
        age = int(input("Enter the age: "))
        shoe = int(input("Enter the shoe size: "))
        data_set[name] = {"age": age, "Shoe size": shoe}
        pass
    display_name = str.capitalize(
        input("Enter a name to display age and shoe size: \n"))
    print(data_set[display_name])
    pass


data_collect()
