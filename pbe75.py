def number_list():
    numbers = [123, 234, 456, 789]
    for i in numbers:
        print(i)
        pass
    user_number = int(input("Enter a 3 digit number: "))
    if user_number in numbers:
        print("The number ", user_number,
              "is in position ", numbers.index(user_number))
        pass
    else:
        print("That is not in the list")
        pass
    pass


number_list()
