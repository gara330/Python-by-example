def printer():
    name = str.capitalize(input("Enter your name: "))
    number = int(input("How many times do you want to print it? "))
    for i in range(number):
        print(name)

printer()
