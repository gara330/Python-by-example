def sport_list():
    sports = ["Basketball", "Football", "Tennis"]
    user_sport = str.capitalize(input("What's your favorite sport? \n"))
    if user_sport in sports:
        print("Your sport is already in the list \n")
        pass
    else:
        sports.append(user_sport)
        print("\n")
        pass
    for i in sports:
        print(i)
        pass
    pass


sport_list()
