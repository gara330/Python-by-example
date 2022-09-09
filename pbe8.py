def billDivider():
    totalBill = int(input("What's the total of the bill? \n"))
    persons = int(input("How many people are on the table? \n"))
    billPerPerson = totalBill/persons
    print("You must pay", billPerPerson,"per person")

    
billDivider()