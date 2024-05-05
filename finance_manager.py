class FinanceManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.records = self.file_handler.read_records()

    def add_record(self, record):
        """Метод добавления записи."""
        self.records.append(record)
        self.file_handler.write_record(record)

    def edit_record(self, index, new_record):
        """Метод редактирования записи."""
        self.records[index] = new_record
        self.file_handler.write_record(self.records)

    def search_records(self, date=None, category=None, amount=None):
        """Метод поиска по категориям, дате или сумме."""
        filtered_records = self.records
        if date:
            filtered_records = [r for r in filtered_records if r.date == date]
        if category:
            filtered_records = [r for r in filtered_records if r.category == category]
        if amount:
            filtered_records = [r for r in filtered_records if r.amount == amount]
        return filtered_records

    def get_balance(self):
        """Метод вывода текущего баланса."""
        income = sum(x.amount for x in self.records if x.category == 'доход')
        expenses = sum(x.amount for x in self.records if x.category == 'расход')
        return income - expenses