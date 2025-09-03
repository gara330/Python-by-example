import csv

def add_book():
    file = open("books.csv", "a")
    new_book = str.capitalize(input("Enter a new book: "))
    new_author = str.capitalize(input("Enter the author of the book: "))
    new_year = str.capitalize(input("Enter the year of the book: "))
    new_record = new_book + "," + new_author + "," + new_year + "\n" 
    file.write(new_record)
    file.close()
    reader = open("books.csv", "r")
    for row in reader:
        print(row)
        pass
    reader.close()
    pass


add_book()
