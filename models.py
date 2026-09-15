class Transaction:
    total_transactions = 0
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category 
        Transaction.total_transactions += 1

    def __str__(self):
        return f"Date: {self.date} | Description: {self.description} | Amount: {self.amount} | Category: {self.category}"

    def is_income(self):
        if self.amount > 0:
            return True
        else:
            return False

    def formatted(self):
        return f"{self.date} {self.description}  {self.amount:.2f} {self.category}"

class RecurringTransaction(Transaction):
    def __init__(self, date, description, amount, category, interval):
        super().__init__(date, description, amount, category)
        self.interval = interval 

    def formatted(self):
        return f"{super().formatted()} {self.interval}"
