import random


def gen_arr():
    float_arr = []
    for i in range(0, 5):
        float_num = random.uniform(10, 100)
        float_num = round(float_num, 2)
        float_arr.append(float_num)
        pass
    return float_arr
    pass


def ask_user():
    while True:
        num = int(input("enter a number between 2 and 5: "))
        if num > 1 & num < 6:
            return num
            break
            pass
        else:
            print("not in the range tray again... \n")
        pass
    pass


def divide(float_arr, num):
    print(float_arr)
    for i in range(len(float_arr)):
        ans = float_arr[i]/num
        print(round(ans, 2))
        pass
    pass


divide(gen_arr(), ask_user())
