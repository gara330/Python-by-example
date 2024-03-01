def bill_divider():
    total_bill = int(input("What's the total of the bill? \n"))
    persons = int(input("How many people are on the table? \n"))
    bill_per_person = total_bill / persons
    print("You must pay", bill_per_person, "per person")


bill_divider()
