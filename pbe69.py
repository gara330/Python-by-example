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

    pass


countries_tuples()
