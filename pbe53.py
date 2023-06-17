import random

def fruit():
    fruit = ["apple", "mandarine", "grape", "melon", "banana"]
    r_fruit = random.choice(fruit)
    return r_fruit

print(fruit())
