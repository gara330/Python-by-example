def dis_poem():
    poem = "The night is beautiful, so the faces of my people. The starts are beautiful so the eyes of my people"
    print("This is the hole poem: \n", poem)
    start = int(input("Enter de initial point to print it: "))
    start = start - 1
    final = int(input("Enter de final pont to print it: "))
    final = final - 1
    print(poem[start:final])

    pass


dis_poem()
