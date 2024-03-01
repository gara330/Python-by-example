def latin_pig():
    vowels = ("a", "e", "i", "o", "u")
    word = str.lower(input("Enter a word to translate to latin pig \n"))
    f_letter = word[0]
    leng = len(word)
    if f_letter in vowels:
        new_word = word + "way"
        print(new_word)
        pass
    else:
        restWord = word[1:leng]
        new_word = restWord + f_letter + "ay"
        print(new_word)
        pass
    pass


latin_pig()
