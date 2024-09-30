from array import *


def nums_array():
    nums = array("i", [])
    for i in range(0, 5):
        n_number = int(input("Enter a number: "))
        nums.append(n_number)
        pass
    nums = sorted(nums)
    print(nums)
    nums.reverse()
    print(nums)
    pass


nums_array()
