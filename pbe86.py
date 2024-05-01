def matching():
    password1 = input("Enter a password: ")
    password2 = input("Enter the password again: ")
    if password1 == password2:
        print("Thank you")
        pass
    elif password1.islower() == password2.islower():
        print("The passwords must be the same case")
        pass
    else:
        print("Incorrect")
        pass
    pass


matching()
