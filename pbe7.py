def ask_user_info():
    u_name = input("What's your name? \n")
    u_age = int(input("How old are you? \n"))
    u_new_age = u_age + 1
    print(u_name, "Next year you are gonna be ", u_new_age)


ask_user_info()
