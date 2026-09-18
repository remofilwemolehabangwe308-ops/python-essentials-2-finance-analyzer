from models import Transaction
from models import RecurringTransaction
from parser import generate_sample_file
from parser import load_transactions
from analytics import running_balance
from analytics import find_duplicates
from analytics import find_outliers
from analytics import category_totals 
from reporting import monthly_summary

valid_transactions = []
rejections = []


while True:
    print(f"===== STUDENT FINANCE ANALYZER =====\n1.Generate a messy sample statement file\n2.Load and validate transactions(reject bad rows)\n3.Show running balance(ledger)\n4.Category breakdown(income vs expenses by tag)\n5.Detect duplicate transactions\n6.Flag unusual transaction(statistical outliers)\n7.Monthly summary report\n8.Run self-test\n9.Exit")

    try:
        option = int(input("Enter option: "))
    except ValueError:
        print("Invalid option")
        continue

    if option == 1:
        generate_sample_file()
        print("Transaction generated successfully")

    elif option == 2:
        valid_transactions, rejections = load_transactions("data/statement.txt")
        if len(valid_transactions) == 0:
            print("No transaction available")
        else:  
          print("Transactions loaded successfully")

    elif option == 3:
        if len(valid_transactions) == 0:
            print("No transaction available")
        else:
         for balance in running_balance(valid_transactions):
            print(balance)
       
    elif option == 4:
        if len(valid_transactions) == 0:
            print("No transaction available")
        else:
         category_breakdown = category_totals(valid_transactions)
         for category, amount in category_breakdown.items():
            print(category, amount)

    elif option == 5:
        duplicates = find_duplicates(valid_transactions)
        for duplicate in duplicates:
            print(duplicate)

    elif option == 6:
        outliers = find_outliers(valid_transactions)
        if len(outliers) == 0:
            print("No outliers available")
        else:
         for outlier in outliers:
            print(outlier)

    elif option == 7:
        monthly_summary(valid_transactions, rejections)
        print("Monthly report generated successfully")

    elif option == 8:
       try:
           import tests
           print("All tests passed")
       except AssertionError:
           print("A test failed")

    elif option == 9:
        print("Goodbye!!!")
        break 
    else:
        print("Invalid option")
