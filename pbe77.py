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
            print("You invited ", guess)
            break
        pass
    uninvite = str.capitalize(input("Type a name: \n"))
    invite_index = guess.index(uninvite)
    print("That person is in position: ", invite_index)
    keep_inivite = str.lower(
        input("Do you still want to invite this person? "))
    if keep_inivite == "no" or keep_inivite == "n":
        del guess[invite_index]
        print(guess)
        pass
    else:
        print(guess)
        pass
    pass


invite()
