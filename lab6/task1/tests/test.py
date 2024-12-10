from lab6.task1.src.main import process_operations

def test_process_operations():
    # Тест 1: Базовые операции
    # Given (исходные данные)
    operations = [
        ('A', 1),  # Добавить 1
        ('A', 2),  # Добавить 2
        ('?', 1),  # Проверить 1
        ('D', 1),  # Удалить 1
        ('?', 1),  # Проверить 1
        ('?', 2),  # Проверить 2
        ('D', 3)   # Удалить 3 (не влияет, так как 3 нет в множестве)
    ]

    # When (выполнение операции)
    result = process_operations(operations)

    # Then (ожидаемый результат)
    assert result == ['Y', 'N', 'Y'], f"Ожидалось ['Y', 'N', 'Y'], но получено {result}"

    # Тест 2: Многократное добавление и удаление одного ключа
    # Given
    operations = [
        ('A', 5),  # Добавить 5
        ('A', 5),  # Повторное добавление 5
        ('?', 5),  # Проверить 5
        ('D', 5),  # Удалить 5
        ('?', 5),  # Проверить 5
        ('D', 5)   # Повторное удаление 5
    ]

    # When
    result = process_operations(operations)

    # Then
    assert result == ['Y', 'N'], f"Ожидалось ['Y', 'N'], но получено {result}"

    # Тест 3: Граничные значения
    # Given
    operations = [
        ('A', 10**18),   # Добавить 10^18
        ('?', 10**18),   # Проверить 10^18
        ('D', 10**18),   # Удалить 10^18
        ('?', 10**18),   # Проверить 10^18
        ('?', -10**18),  # Проверить -10^18
    ]

    # When
    result = process_operations(operations)

    # Then
    assert result == ['Y', 'N', 'N'], f"Ожидалось ['Y', 'N', 'N'], но получено {result}"

    # Тест 4: Пустой список операций
    # Given
    operations = []

    # When
    result = process_operations(operations)

    # Then
    assert result == [], f"Ожидалось [], но получено {result}"

    # Тест 5: Дублирующиеся операции
    # Given
    operations = [
        ('A', 3),  # Добавить 3
        ('?', 3),  # Проверить 3
        ('A', 3),  # Повторное добавление 3
        ('?', 3),  # Проверить 3
        ('D', 3),  # Удалить 3
        ('?', 3),  # Проверить 3
    ]

    # When
    result = process_operations(operations)

    # Then
    assert result == ['Y', 'Y', 'N'], f"Ожидалось ['Y', 'Y', 'N'], но получено {result}"