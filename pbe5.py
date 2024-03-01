def adder():
    num1 = int(input("Enter a number: \n"))
    num2 = int(input("Entere a number to add: \n"))
    addResult = num1 + num2
    print("The add is:", addResult)
    return addResult


def multiplaier():
    add = adder()
    num3 = int(input("Enter a number to multiply the add \n"))
    result = add * num3
    print("The last result is:", result)
    pass


def main():
    multiplaier()


main()
