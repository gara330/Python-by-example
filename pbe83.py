def upper():
    while True:
        user_word = str(input("Enter a word in uppercase: "))
        if user_word.isupper():
            print("Thank you")
            break
        else:
            print("Is not upper case, try again... ")
            pass
        pass
    pass


upper()
