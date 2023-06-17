def g_bottles():
    bottles = 3
    while bottles != 0:
        print("There are ", bottles, "green bottles hanging on the wall, ", 
            bottles, "green bottles hanging on the wall, and if 1 green bottle should accidentally falls"
            )
        bottles = bottles -1
        while True:
            answer = int(input("How many  green bottles will be hanging on the wall? "))
            if answer != bottles:
                print("Wrong answer, try again")
                pass
            else:
                break
        pass
    print("There ar no more green bottles hanging on the wall")
    pass

g_bottles()
