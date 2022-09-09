def askUserInfo():
    uName = input("What's your name? \n")
    uAge = int(input("How old are you? \n"))
    uNewAge = uAge + 1
    print(uName, "Next year you are gonna be ", uNewAge)
    
askUserInfo()