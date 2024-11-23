import random

def add_arrays():
    nums = []
    user_nums = []
    for x in range(0,5):
        rand_num = random.randint(0,10)
        nums.append(rand_num)
        pass
        
    for i in range(0,3):
        numb = int(input("Enter one number: "))
        user_nums.append(numb)
        pass
    new_array = user_nums + nums
    new_array = sorted(new_array)
    for j in new_array:
        print(j)
        pass
    pass

add_arrays()
