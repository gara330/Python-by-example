def matriz():
    arr = [
        [2, 5, 8],
        [3, 7, 4],
        [1, 6, 9],
        [4, 2, 0]
    ]
    row = int(input("select a row: "))
    print(arr[row])
    col = int(input("select a column: "))
    print(arr[row][col])
    while True:
        change = str.capitalize(
            input("do you want to change the value? y,n: "))
        if change == "Y" or change == "N":
            break
            pass

        pass
    if change == "Y":
        new_number = int(input("enter the new value: "))
        arr[row][col] = new_number
        pass
    print(arr[row])
    pass


matriz()
