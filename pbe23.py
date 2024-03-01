def rhyme():
    n_rhime = input("Tell me a nursery rhyme \n")
    len_rhyme = len(n_rhime)
    print("The length is", len_rhyme)
    start_number = int(input("Enter a starting number: \n"))
    end_number = int(input("Enter an ending number: \n"))
    print(n_rhime[start_number - 1 : end_number + 1])
    pass


rhyme()
