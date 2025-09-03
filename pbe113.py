import csv

def new_records():
    appends = int(input("How many books do you want to add: "))
    file = open("books.csv", "a")
    for i in range(0,appends):
        new_book = str.capitalize(input("Enter a new book: "))
        new_author = str.capitalize(input("Enter the author of the book: "))
        new_year = str.capitalize(input("Enter the year of the book: "))
        new_record = new_book + "," + new_author + "," + new_year + "\n" 
        file.write(new_record)
        pass
    file.close()
    pass


def searh():
    count = 0
    file = open("books.csv", "r")
    author = str.capitalize(input("Searh for an author: "))
    for row in file:
        if author in str(row):
            print(row)
            count += 1
            pass
        pass
    if count == 0:
       print("There is no books from that author")
       pass
    file.close()
    pass


new_records()
searh()
