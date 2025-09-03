import csv

def books_table():
    file = open("books.csv", "w")
    file.write("To kill a mockingbird, Harper Lee, 1960 \n")
    file.write("A brief History of time, Stephen Hawking, 1988 \n")
    file.write("The great Gatsby, F. Scott Fitzgerald, 1922 \n")
    file.write("The man who mistook his wife for a hat, Oliver Sacks, 1985 \n")
    file.write("Pride and Prejudice, Jane Austen, 1813 \n")
    file.close()
    pass


books_table()
