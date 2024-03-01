def inviter():
    total_guest = 0
    while True:
        name = str.capitalize(input("Who do you want to invite to the party? "))
        total_guest = total_guest + 1
        print(name, "has been invited, total of guest = ", total_guest)
        answer = str.lower(input("Do you want to invite some else? y/n "))
        if answer == "y" or answer == "yes":
            pass
        else:
            break
            pass
        pass
    pass


inviter()
