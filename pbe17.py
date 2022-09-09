def askAge():
    age = int(input("How old are you? \n"))
    if age >= 18:
        print("You can vote \n")
        pass
    elif age == 17:
        print("You can learn to drive \n")
        pass
    elif age == 16:
        print("You can buy a lottery ticket \n")
        pass
    else:
        print("You can go Trick-or-Treating \n")
        pass
    pass

askAge()