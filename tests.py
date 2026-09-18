from models import Transaction
from parser import load_transactions
from analytics import running_balance
from analytics import make_flagger
from analytics import find_duplicates
from analytics import category_totals
from analytics import find_outliers

transaction1 = Transaction("2026-08-12","Netflix",-100,"Entertainment")
assert transaction1.description == "Netflix"
assert transaction1.is_income() == False

transaction2 = Transaction("2026-08-03","Freelance income",2500,"Income")
assert transaction2.is_income() == True

with open("data/test_valid.txt", "w") as file:
    file.write("2026-08-07,School supplies,-500,Education")
valid_transactions, rejections = load_transactions("data/test_valid.txt")
assert len(valid_transactions) == 1

assert valid_transactions[0].date == "2026-08-07"

assert valid_transactions[0].amount == -500

assert valid_transactions[0].category == "Education"

with open("data/test_bad_date.txt", "w") as file:
    file.write("2026/08/05,Rent payment,-5000,Housing")
valid_transactions, rejections = load_transactions('data/test_bad_date.txt')
assert valid_transactions[0].date == "2026-08-05"

with open("data/test_junk.txt", 'w') as file:
    file.write(" THIS IS NOT A TRANSACTION")
valid_transactions, rejections = load_transactions("data/test_junk.txt")
assert len(valid_transactions) == 0
assert len(rejections) == 1

with open("data/test_missing.txt", "w") as file:
    file.write('2026-08-10,Products,-1000')
valid_transactions, rejections = load_transactions("data/test_missing.txt")
assert len(valid_transactions) == 0
assert len(rejections) == 1

with open("data/test_bad_amount.txt", "w") as file:
    file.write("2026-08-11,Airtime,xyz,Communication")
valid_transactions, rejections = load_transactions("data/test_bad_amount.txt")
assert len(valid_transactions) == 0
assert len(rejections) == 1

transaction4 = Transaction("2026-08-01","Electricity",-200,"Bills")
transaction5 = Transaction("2026-08-05","Freelancing Income",500,"Income")
transaction6 = Transaction("2026-08-05","Products",-150,"SkinCare")
transactions = [transaction4, transaction5, transaction6]
balances = list(running_balance(transactions))
assert balances == [-200, 300, 150]

flagger = make_flagger(1000)
transaction7 = Transaction("2026-08-09","Monthly salary",5000,"Income")
assert flagger(transaction7)  == True 
assert flagger(transaction4) == False

transaction8 = Transaction("2026-08-01","Electricity",-200,"Bills")
transactions.append(transaction8)
duplicates = list(find_duplicates(transactions))
assert duplicates == [transaction8]

totals_of_categories = category_totals(transactions)
assert totals_of_categories["Bills"] == -400
assert totals_of_categories["Income"] == 500

transaction9 = Transaction("2026-08-09","Electricity",-100,"Bills")
transaction10 = Transaction("2026-08-10","Airtime",-50,"Communication")
transactions = [transaction4, transaction5, transaction6, transaction7, transaction9, transaction10]
outlier = list(find_outliers(transactions))
assert outlier == [transaction7]

    

