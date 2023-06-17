def guesser():
    compnum = 50
    counter = 0
    guess = 0
    while guess != compnum:
        guess = int(input("Ente your guess: "))
        if guess > compnum:
            print("To high")
            pass
        elif guess < compnum:
            print("to low")
            pass
        print("That's it!")
        pass
    pass

guesser()
