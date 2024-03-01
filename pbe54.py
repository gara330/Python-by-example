import random


def heads_or_tails():
    coin = ["heads", "tails"]
    machine = random.choice(coin)
    return machine


def game():
    machine = heads_or_tails()
    user = str.lower(input("Choose heads or tails: [h/t] "))
    if user == "h":
        user = "heads"
        pass
    elif user == "t":
        user = "tails"
        pass
    else:
        print("Not a valid answer")
        exit

    if user == machine:
        print("You win!")
        pass
    else:
        print("Bad luck")
        pass
    print("The machine got: ", machine)


game()
