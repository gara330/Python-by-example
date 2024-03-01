import random


def math_quiz():
    score = 0
    for i in range(1, 6):
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        correct_number = number1 + number2
        print("Cuestion: ", i, "\n", number1, "+", number2)
        answer = int(input("\n"))
        if correct_number == answer:
            score += 1
            pass
        pass
    print("Your score is: ", score, "\n")

    pass


math_quiz()
