from typing import List, Tuple
from models import FinanceRecord
from file_handler import FileHandler


class FinanceManager:
    """
    Класс реализует основную логику приложения,
    включая добавление, редактирование, поиск и вычисление баланса.
    """
    def __init__(self, file_handler: [FileHandler]):
        self.file_handler = file_handler
        self.records = self.file_handler.read_records()

    def add_record(self, record: FinanceRecord) -> None:
        """Метод добавления записи."""
        self.records.append(record)
        self.file_handler.write_record(record)

    def edit_record(self, index: int, new_record: FinanceRecord) -> None:
        """Метод редактирования записи."""
        self.records[index] = new_record
        self.file_handler.write_record(self.records)

    def search_records(self, date: str = None, category: str = None, amount: float = None) -> List:
        """Метод поиска по категориям, дате или сумме."""
        filtered_records = self.records
        if date:
            filtered_records = [r for r in filtered_records if r.date == date]
        if category:
            filtered_records = [r for r in filtered_records if r.category == category]
        if amount:
            filtered_records = [r for r in filtered_records if r.amount == amount]
        return filtered_records

    def get_balance(self) -> float:
        """Метод вычисления текущего баланса."""
        incomes, expenses = self.get_incomes_and_expenses()
        return incomes - expenses

    def get_incomes_and_expenses(self) -> Tuple[float, float]:
        """Метод вывода дохода и расхода."""
        incomes = 0
        expenses = 0
        for record in self.records:
            if record.category == "Доход":
                incomes += record.amount
            elif record.category == "Расход":
                expenses += record.amount
        return incomes, expenses
