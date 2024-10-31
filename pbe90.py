def five_array():
    num_array = []
    counter = 0
    while counter < 5:
        num = int(input("Enter a number to add to the array: "))
        if num > 9 and num < 21:
            num_array.append(num)
            counter = counter + 1
            pass
        else:
            print("Out of range")
            pass
        pass
    for i in num_array:
        print(i)
        pass
    pass


five_array()
