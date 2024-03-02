def school_subjects():
    subjects = ["Math", "Spanis", "Chemestry", "Phisics", "Cs", "Algebra"]
    for i in subjects:
        print(i)
        pass
    disklike = str.capitalize(input("Which of the subjects above you don't like \n:"))
    if disklike in subjects:
        disklike = subjects.index(disklike)
        del subjects[disklike]
        pass
    else:
        print("That subject is not in the list")
        pass
    for x in subjects:
        print(x)
        pass
    pass


school_subjects()
