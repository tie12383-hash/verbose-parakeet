"""основной модуль для демонстрации работы"""

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> None:
    """основная функция для демонстрации работы модуля"""
    print("=== Демонстрация маскировки карт и счетов ===\n")

    test_data = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
    ]

    for data in test_data:
        print(f"Вход: {data}")
        print(f"Выход: {mask_account_card(data)}\n")

    print("\n=== Демонстрация обработки операций ===\n")

    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("Отфильтрованные операции (EXECUTED):")
    for op in filter_by_state(operations):
        print(f"ID: {op['id']}, Date: {get_date(op['date'])}, State: {op['state']}")

    print("\nОтсортированные операции (по убыванию даты):")
    for op in sort_by_date(operations):
        print(f"ID: {op['id']}, Date: {get_date(op['date'])}, State: {op['state']}")


if __name__ == "__main__":
    main()
