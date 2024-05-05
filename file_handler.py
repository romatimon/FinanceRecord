from typing import List
from models import FinanceRecord


class FileHandler:
    """Класс отвечает за чтение и запись в текстовый файл."""
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_records(self) -> List[FinanceRecord]:
        """Метод чтения файла."""
        records = []
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    date, category, amount, description = line.strip().split(',')
                    record = FinanceRecord(date, category, float(amount), description)
                    records.append(record)
        except FileNotFoundError:
            print('Ошибка обработки файла.')
        return records

    def write_record(self, records: List[FinanceRecord]):
        """Метод записи в файл."""
        if isinstance(records, list):
            with open(self.file_path, 'w') as file:
                for record in records:
                    file.write(f"{record.date},{record.category},{record.amount},{record.description}\n")
        else:
            with open(self.file_path, 'a') as file:
                file.write(f"{records.date},{records.category},{records.amount},{records.description}\n")
