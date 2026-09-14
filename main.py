#EXPENSE TRACKER PROJECT

expenses = [] 
print("  WELCOME TO EXPENSE TRACKER!!  ")

while True:
    print("----MENU----")
    print("1.Add Expenses")
    print("2.View all Expenses")
    print("3.View Total Expenses")
    print("4.Exit")

    choice=int(input("Please Enter Your Choice: "))
    if(choice==1):
        date=input("Enter the Date: ")
        category=input("What type of Expense? ")
        description=input("In what you made this Expense? ")
        amount=float(input("Enter the amount: "))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print(" \nExpense is added successfully!! ")
    elif(choice==2):
        if( len(expenses)==0 ):
            print(" No Expenses Added!! ")
        else:
            print("----Your all Expenses is Displayed here---- ")
            count=1
            for everyexpense in expenses:
                print(f"Expense Number {count} -> {everyexpense["date"]},{everyexpense["category"]},{everyexpense["description"]},{everyexpense["amount"]}")  
                count=count+1

    elif(choice==3):
        total=0
        for eachexpense in expenses:
            total=total+eachexpense["amount"]
        print("\nTOTAL EXPENSE = ",total)

    elif(choice==4):
        print(" THANK YOU FOR USING THIS SYSTEM!! ")
        break
    else:
        print("Enter a valid number from 1 to 4!!")
