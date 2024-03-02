def invite():
    guess = []
    print("Invite 3 people to your party: \n")
    for i in range(0, 3):
        inv = str.capitalize(input("Who do you want to invite? "))
        guess.append(inv)
        pass
    while True:
        keep_going = str.lower(input("Do you want to keep going? [yes/no]"))
        if keep_going == "yes" or keep_going == "y":
            inv = str.capitalize(input("Who do you want to invite? "))
            guess.append(inv)
            pass
        else:
            print("You invited ", len(guess), "people")
            break
        pass
    pass


invite()
