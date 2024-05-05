from models import FinanceRecord

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_records(self):
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

    def write_record(self, record):
        with open(self.file_path, 'w') as file:
            for attr in record:
                file.write(f"{attr.date},{attr.category},{attr.amount},{attr.description}\n")
