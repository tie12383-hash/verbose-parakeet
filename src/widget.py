"""модуль для работы с виджетом банковских операций"""

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    маскировка номера карты или счета в указанной строке

    Args:
        account_info: Строка с информацией о карте или счете
                     (например, "Visa Platinum 7000792289606361")

    Returns:
        Строка с замаскированным номером
    """
    # разделение строки на части
    parts = account_info.split()

    # последний элемент - номер
    number_str = parts[-1]

    # все что перед последним элементом - это название
    name = " ".join(parts[:-1])

    # определение типа по названию и использование маскировки
    if name.lower() == "счет":
        masked_number = get_mask_account(int(number_str))
    else:
        masked_number = get_mask_card_number(int(number_str))

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    преобразование даты из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string: Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        Дата в формате "11.03.2024"
    """
    # разделение даты и времени
    date_part = date_string.split("T")[0]

    # разбор даты на компоненты
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
