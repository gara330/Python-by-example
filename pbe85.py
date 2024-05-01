def vowels():
    name = str.capitalize(input("Enter your name: "))
    count = 0
    for letter in name:
        if (
            letter == "a"
            or letter == "e"
            or letter == "i"
            or letter == "o"
            or letter == "u"
        ):
            count = count + 1
            pass
        pass
    print("There is ", count, "vowels in your name")
    pass


vowels()
