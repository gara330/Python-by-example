import math

def square_root():
    number = int(input("Enter a number over 500: "))
    answer = math.sqrt(number)
    print(round(answer, 2))
    pass

square_root()
