def how_many_times():
    largeNumber = int(input("Enter a number over 100 \n"))
    smallNumber = int(input("Enter a number under 10 \n"))
    hTimes = largeNumber//smallNumber
    print(smallNumber,"goes in", largeNumber, hTimes,"times")
    pass   
    
how_many_times()
