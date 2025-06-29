def matriz():
    arr = [
        [2, 5, 8],
        [3, 7, 4],
        [1, 6, 9],
        [4, 2, 0]
    ]
    row = int(input("select a row: "))
    print(arr[row])
    new_number = int(input("enter a new number to the row: "))
    arr[row].append(new_number)
    print(arr[row])
    pass


matriz()
