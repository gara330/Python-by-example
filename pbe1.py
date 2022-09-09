def askFirsName():
    name = input("What's you name? \n")
    return name

def sayHello(name):
    print("Hello", name)
    pass

def main():
    name = askFirsName()
    sayHello(name)
    pass

main()