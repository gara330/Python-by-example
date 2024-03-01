import random


def ran_numb():
    com_number = int(random.randint(1, 5))

    tries = 0
    while tries < 2:
        us_number = int(input("Chose a number between 1-5: "))
        if us_number == com_number:
            print("Well done! ")
            exit()
        elif us_number > com_number:
            print("To high! ")
            tries += 1
            pass
        elif us_number < com_number:
            print("To low! ")
            tries += 1
            pass
        pass
    print("You lose!")
    pass


ran_numb()
