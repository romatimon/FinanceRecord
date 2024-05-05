class FinanceRecord:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.date}, {self.category}, {self.amount}, {self.description}"
