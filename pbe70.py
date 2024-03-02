def countries_tuples():
    countries = ("Mexico", "Canada", "Alemania", "Japon", "Korea")
    print("Choose one of these countries to show it index: ")
    for i in countries:
        print(i)
        pass
    user_country = str.capitalize(input("\n:"))
    if user_country in countries:
        print(countries.index(user_country))
        pass
    else:
        print("Your country is not in the tuple")
        pass

    user_number = int(input("Now enter a number: "))
    if user_number < len(countries) - 1:
        print("The country in that position is: ", countries[user_number])
        pass
    else:
        print("Invalid number")
        pass

    pass


countries_tuples()
