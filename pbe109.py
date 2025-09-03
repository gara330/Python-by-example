def menu():
    while True:
        print(
            "1) Create a new file \n",
            "2) Display the file \n",
            "3) Add a new item to the file \n"
        )
        user_opt = int(input( "Make a selection 1, 2 or 3: "))
        if user_opt == 1 or user_opt == 2 or user_opt == 3:
            return user_opt
            break
            pass
        else:
            print("\n Select a correct value, try again... \n")
            pass
        pass
    pass


def new_file():
    file = open("subject.txt", "w")
    subject = str.capitalize(input("Enter a school subject: "))
    file.write(subject)
    file.close()
    pass

def read_file():
    file = open("subject.txt", "r")
    print(file.read())
    file.close
    pass


def apend_file():
    file = open("subject.txt", "a")
    subject = str.capitalize(input("Enter a new subject: "))
    file.write("\n")
    file.write(subject)
    file.close()
    pass

menu = menu()

if menu == 1:
    new_file()
    pass
if menu == 2:
    read_file()
    pass
elif menu == 3:
    apend_file()
    pass
