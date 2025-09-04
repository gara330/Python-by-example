import csv

def year_search():
    file = list(csv.reader(open("books.csv")))
    init_year = int(input("Enter the starting year for the search: "))
    end_year = int(input("Enter the end year for the search: "))
    books = []
    for row in file:
        books.append(row)
        pass

    count = 0
    for row in books:
        if int(books[count][2]) >= init_year and int(books[count][2]) <= end_year:
            print(books[count])
            pass
        count += 1
        pass
    pass


year_search()
