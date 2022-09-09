def latinPig():
    vowels = ["a","e","i","o","u"]
    word = str.lower(input("Enter a word to translate to latin pig \n"))
    fLetter = word[0]
    leng = len(word)
    if fLetter in vowels:
        newWord = word + "way"
        print(newWord)
        pass
    else:
        restWord = word[1:leng]
        newWord = restWord + fLetter + "ay"
        print(newWord)
        pass
    pass

latinPig()