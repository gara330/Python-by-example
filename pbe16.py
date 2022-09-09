def askForRain():
    rain = str.lower(input("It's raining outside? \n"))
    if rain == "yes":
        windy = str.lower(input("It's too windy? \n"))
        if windy == "yes":
            print("It's too windy for an umbrella")
            pass
        else:
            print("Take an umbrella")
            pass
        pass
    else:
        print("Enjoy your day")
        pass
    pass

askForRain()