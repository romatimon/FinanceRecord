class FinanceRecord:
    """
    Класс, представляющий финансовую запись.
    Атрибуты:
    date (str): Дата записи в формате 'YYYY-MM-DD'.
    category (str): Категория записи ('Доход' или 'Расход').
    amount (float): Сумма записи.
    description (str): Описание записи.
    """
    def __init__(self, date: str, category: str, amount: float, description: str):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.date}, {self.category}, {self.amount}, {self.description}"
