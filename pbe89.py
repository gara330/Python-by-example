import random


def rand_intergers():
    numb_array = []
    for i in range(1, 6):
        num = random.randint(1, 100)
        numb_array.append(num)
        pass
    for x in numb_array:
        print(x)
        pass
    pass


rand_intergers()
