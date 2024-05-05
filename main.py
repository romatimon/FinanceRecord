from finance_manager import FinanceManager
from file_handler import FileHandler
from models import FinanceRecord

FILE_PATH = 'finance_records.txt'


def main():
    file_handler = FileHandler(FILE_PATH)
    finance_manager = FinanceManager(file_handler)
    #
    # date = input("Дата (ГГГГ-ММ-ДД): ")
    # category = input("Категория (доход/расход): ")
    # amount = int(input("Сумма: "))
    # description = input("Описание: ")
    # record = FinanceRecord(date, category, amount, description)
    # finance_manager.add_record(record)
    # print('Запись успешно добавлена.')

    for i, record in enumerate(finance_manager.records):
        print(f"{i}. {record}")
    index = int(input("Выберите запись для редактирования: "))
    date = input("Новая дата (ГГГГ-ММ-ДД): ")
    category = input("Новая категория (доход/расход): ")
    amount = int(input("Новая сумма: "))
    description = input("Новое описание: ")
    new_record = FinanceRecord(date, category, amount, description)
    finance_manager.edit_record(index, new_record)
    print("Запись успешно обновлена!")


if __name__ == '__main__':
    main()