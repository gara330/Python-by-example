def num_file():
    file = open ("numbers.txt", "w")
    file.write("1, 2, 3, 4, 5")
    file.close()
    pass


def read_file():
    file = open ("numbers.txt", "r")
    print(file.read())
    pass
    

num_file()
read_file()
