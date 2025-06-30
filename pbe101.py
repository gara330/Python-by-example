def data_sales():
    sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
             "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
             "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
             "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
    for name in sales:
        print((name), sales[name])
        pass
    return sales
    pass


def sales(sales):
    name = str.capitalize(input("enter a name: "))
    region = str.capitalize(input("enter a region: "))
    print((name), sales[name][region], "\n")
    pass


def new_sales(sales):
    name = str.capitalize(input("select a name: "))
    region = str.capitalize(input("select a region to change the data: "))
    new_value = int(input("enter the new sales value: "))
    sales[name][region] = new_value
    print((name), sales[name])
    pass


sales(data_sales())
new_sales(data_sales())
