def reverse():
    user_word = input("Enter a word to display it backwards: ")
    reversed = user_word[::-1]
    for letter in reversed:
        print(letter)
    pass


reverse()
