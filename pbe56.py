import random


def random_picker():
    rand_number = int(random.randint(1, 10))
    user_number = 0
    while rand_number != user_number:
        user_number = int(
            input("Enter a number between 1 and 10 until you guess the rigth one: \n")
        )
        if rand_number == user_number:
            print("You got it!")
            pass
        pass
    pass


random_picker()
