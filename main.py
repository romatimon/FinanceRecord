from finance_manager import FinanceManager
from file_handler import FileHandler
from models import FinanceRecord

FILE_PATH = 'finance_records.txt'


def main():
    file_handler = FileHandler(FILE_PATH)
    finance_manager = FinanceManager(file_handler)

    while True:
        print("Выберите действие:")
        print("1. Показать баланс")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")

        choice = input('Ваш выбор: ')

        if choice == '1':
            balance = finance_manager.get_balance()
            print(f'Текущий баланс: {balance}')
        elif choice == '2':
            date = input("Дата (ГГГГ-ММ-ДД): ")
            category = input("Категория (доход/расход): ")
            amount = int(input("Сумма: "))
            description = input("Описание: ")
            record = FinanceRecord(date, category, amount, description)
            finance_manager.add_record(record)
            print('Запись успешно добавлена.')
        elif choice == '3':
            for i, record in enumerate(finance_manager.records):
                print(f"{i}. {record}")
            index = int(input("Выберите запись для редактирования: "))
            date = input("Новая дата (ГГГГ-ММ-ДД): ")
            category = input("Новая категория (доход/расход): ")
            amount = int(input("Новая сумма: "))
            description = input("Новое описание: ")
            new_record = FinanceRecord(date, category, amount, description)
            finance_manager.edit_record(index, new_record)
            print("Запись успешно обновлена.")
        elif choice == '4':
            date = input("Дата (ГГГГ-ММ-ДД) (необязательно): ")
            category = input("Категория (доход/расход) (необязательно): ")
            amount = input("Сумма (необязательно): ")
            filtered_records = finance_manager.search_records(date=date, category=category, amount=amount)
            for record in filtered_records:
                print(record)


if __name__ == '__main__':
    main()