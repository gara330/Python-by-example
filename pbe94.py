import random


def position_number():
    nums = []
    for i in range(0, 5):
        num = int(random.randint(0, 10))
        nums.append(num)
        pass
    while True:
        print(nums, "\n")
        user_num = int(input("select a number on the list: "))
        if user_num in nums:
            print(nums.index(user_num))
            break
        else:
            print("number not in the list, try again... \n")
        pass
    pass


position_number()
