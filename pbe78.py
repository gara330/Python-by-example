def tv_show():
    shows = ["Invincible", "Criminal Minds", "Breaking Bad", "Naruto"]
    printer(shows)
    user_show = str.capitalize(input("Enter a new tv show: "))
    new_show_index = int(input("Enter a position for the show: "))
    shows.insert(new_show_index, user_show)
    printer(shows)
    pass


def printer(shows):
    for i in shows:
        print(i)
        pass
    pass


tv_show()
