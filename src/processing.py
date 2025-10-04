"""модуль для обработки данных банковских операций"""

from typing import List, Dict, Any


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    фильтрация операции по статусу

    Args:
        operations: Список словарей с операциями
        state: Статус для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список операций
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """
    сортировка операции по дате

    Args:
        operations: Список словарей с операциями
        descending: Порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        Отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda x: x["date"],
        reverse=descending,
    )
