class FinanceManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.records = self.file_handler.read_records()

    def add_record(self, record):
        self.records.append(record)
        self.file_handler.write_record(record)

    def edit_record(self, index, new_record):
        self.records[index] = new_record
        self.file_handler.write_record(self.records)
