def askForslices():
    initialSlices = int(input("How many slices do you start with? \n"))
    eatenSlices = int(input("How many slives have you eaten? \n"))
    if initialSlices > eatenSlices:
        slicesLeft = initialSlices - eatenSlices
        print("You still have ", slicesLeft, "left, queep going \n")
        pass
    else:
        print("That's impossible dude, try latter")
    pass

def main():
    askForslices()
    pass

main()
