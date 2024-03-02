def food_dictionary():
    foods = {}
    for i in range(1, 5):
        user_food = str.lower(input("Enter a food: \n"))
        foods[i] = user_food
        pass
    print(foods)
    dislike = int(input("Enter the number of the food you want to remove: "))
    del foods[dislike]
    print(foods)
    pass


food_dictionary()
