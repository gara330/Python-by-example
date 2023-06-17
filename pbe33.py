def division():
    number = int(input("Enter a number: "))
    div = int(input("Enter a second number for the division: "))
    answer = number // div
    res = number % div
    print(number,"divided by ", div, "is", answer, "with", res, "remaining")
    pass

division()
