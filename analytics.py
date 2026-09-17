import statistics

def running_balance(transactions):
    balance = 0
    for transaction in transactions:
        balance += transaction.amount
        yield balance 

def make_flagger(threshold):
    def flag(transaction):
        if abs(transaction.amount) >= threshold:
            return True
        else:
            return False 
    return flag

def find_duplicates(transactions):
    transaction_set = set()
    duplicates_transactions = []
    for transaction in transactions:
        signature = (transaction.date, transaction.description, transaction.amount, transaction.category)
        if signature in transaction_set:
            duplicates_transactions.append(transaction)
        else:
            transaction_set.add(signature)
    return duplicates_transactions

def find_outliers(transactions):
    amounts = []
    for transaction in transactions:
        amounts.append(transaction.amount)
    mean = sum(amounts) / len(amounts)
    standard_deviation = statistics.stdev(amounts)
    outlier_transaction = []
    for transaction in transactions:
        if abs(transaction.amount - mean) > 2 * standard_deviation:
            outlier_transaction.append(transaction)
    return outlier_transaction

def category_totals(transactions):
    sum_of_categories = {}
    for transaction in transactions:
        if transaction.category in sum_of_categories:
            sum_of_categories[transaction.category] += transaction.amount
        else:
            sum_of_categories[transaction.category] = transaction.amount
    return sum_of_categories