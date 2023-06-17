def dayDivider():
    days = int(input("How many days do you want to convert? \n"))
    hours = days*24
    minutes = hours*60
    seconds = minutes*60
    
    print("There are", hours, "hours, or", minutes, "minutes, or maybe you wanna know", seconds, "seconds in ", days, "days")
    pass

dayDivider()


