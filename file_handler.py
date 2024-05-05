from models import FinanceRecord


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_records(self):
        """Метод чтения файла."""
        records = []
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    date, category, amount, description = line.strip().split(',')
                    record = FinanceRecord(date, category, int(amount), description)
                    records.append(record)
        except FileNotFoundError:
            pass
        return records

    def write_record(self, records):
        """Метод записи в файл."""
        if isinstance(records, list):
            with open(self.file_path, 'w') as file:
                for record in records:
                    file.write(f"{record.date},{record.category},{record.amount},{record.description}\n")
        else:
            with open(self.file_path, 'a') as file:
                file.write(f"{records.date},{records.category},{records.amount},{records.description}\n")
