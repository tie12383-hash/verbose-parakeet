def get_mask_card_number(card_number: int) -> str:
    """
    маскировка номера банковской карты
    возврат строки в формате 'XXXX XX** **** XXXX'.
    """
    str_number = str(card_number)
    if len(str_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    маскировка номера банковского счета.
    возврат строки в формате '**XXXX'.
    """
    str_number = str(account_number)
    if len(str_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{str_number[-4:]}"
