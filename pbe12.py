def comparator__to_minor():
    numb1 = int(input("Enter a number: \n"))
    numb2 = int(input("Enter one more number: \n"))
    if numb1 > numb2:
        print("The number: ", numb2, "Is lower than: ", numb1)
        pass
    else:
        print("The number: ", numb1, "Is lower than ", numb2)
        pass
    pass


def comparator_to_mayor():
    numb1 = int(input("Enter a number: \n"))
    numb2 = int(input("Enter one more number: \n"))

    if numb1 < numb2:
        print("The number: ", numb2, "Is mayor than: ", numb1)
        pass
    else:
        print("The number: ", numb1, "Is mayor than: ", numb2)
        pass


def main():
    comparator__to_minor()
    comparator_to_mayor()
    pass


main()
