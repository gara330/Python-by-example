def inviter():
    number = int(input("How many people do you want to invite? "))
    if number <= 10:
        for i in range(number):
            name = str.capitalize(input("Enter the name: "))
            print(name, "Have been invited!")
            pass
        pass
    else:
        print("To many people")
        pass
    pass


inviter()
