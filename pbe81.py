def sep_words():
    user_word = str.capitalize(input("What's your favorite school subject? "))
    for letter in user_word:
        print(letter, end="-")
        pass
    pass


sep_words()
