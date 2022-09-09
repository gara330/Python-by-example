from tkinter import N


def rhyme():
    nRhime = input("Tell me a nursery rhyme \n")
    lenNRhyme = len(nRhime)
    print("The length is", lenNRhyme)
    startNumber = int(input("Enter a starting number: \n"))
    endNumber = int(input("Enter an ending number: \n"))
    print(nRhime[startNumber-1:endNumber+1])
    pass

rhyme()