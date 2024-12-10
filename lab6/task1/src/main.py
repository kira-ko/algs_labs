import sys
import os


def process_operations(operations):
    result = []  # Список для хранения результатов операций '?'
    data_set = set()  # Инициализация пустого множества

    for operation in operations:
        op = operation[0]  # Тип операции: 'A', 'D' или '?'
        key = int(operation[1])  # Ключ операции, преобразуем к int для гарантии

        if op == 'A':  # Добавление ключа
            data_set.add(key)
        elif op == 'D':  # Удаление ключа
            data_set.discard(key)
        elif op == '?':  # Проверка существования ключа
            result.append('Y' if key in data_set else 'N')

    return result  # Возвращаем результаты операций '?'



