def new_arras():
    user_arr = []
    for i in range(0, 5):
        numb = int(input("Insert a number: "))
        user_arr.append(numb)
        pass
    user_arr.sort()
    print(user_arr)
    del_numb = int(
        input("Now select a number from above to delete it from the array: "))
    if del_numb in user_arr:
        user_arr.remove(del_numb)
        new_arr = []
        new_arr.append(del_numb)
        print(user_arr, "\n", new_arr)
        pass
    else:
        print("number not in the array")
        pass
    pass


new_arras()
