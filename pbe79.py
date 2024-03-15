def num():
    nums = []
    for i in range(0, 3):
        number = int(input("Enter a number: "))
        nums.append(number)
        print(nums)
        pass
    answer = str.lower(input("Do you wanna keep the last number? [yes,no]"))
    if answer == "no" or answer == "n":
        delete_number = len(nums) - 1
        nums.remove(number)
        print(nums)
        pass
    else:
        print(nums)
        pass
    pass


num()
