def ask_firts_name():
    name = input("What's you name? \n")
    return name


def say_hello(name):
    print("Hello", name)
    pass


def main():
    name = ask_firts_name()
    say_hello(name)
    pass


main()
