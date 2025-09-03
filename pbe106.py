def name_fie():
    file = open("names.txt", "w")
    file.write("Alfred\n")
    file.write("Bruce\n")
    file.write("Clark\n")
    file.write("Peter\n")
    file.write("Anthony\n")
    file.close()
    pass
    
def read_names():
    file = open("names.txt", "r")
    print(file.read())
    file.close()
    pass


name_fie()
read_names()
