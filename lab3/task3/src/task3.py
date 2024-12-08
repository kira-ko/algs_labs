def can_sort_scarecrow(n, k, arr):
    """
    Определяет, можно ли отсортировать массив с помощью "сортировки пугалом".

    :param n: Число матрешек.
    :param k: Размах рук (шаг перемещения).
    :param arr: Список размеров матрешек.
    :return: "ДА", если сортировка возможна, иначе "НЕТ".
    """
    if n == 0 or k <= 0:
        return 'Нет'

    # Разделяем элементы по индексам с одинаковым остатком от деления на k
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(arr[i])

    # Сортируем каждую группу и проверяем общий порядок
    for group in groups:
        group.sort()

    # Собираем массив из отсортированных групп
    sorted_arr = []
    for i in range(n):
        sorted_arr.append(groups[i % k].pop(0))

    # Проверяем, является ли итоговый массив отсортированным
    return sorted_arr == sorted(arr)


if __name__ == "__main__":
    with open('../txtf/input.txt', "r") as file:
        n, k = map(int, file.readline().strip().split())
        arr = list(map(int, file.readline().strip().split()))

    if can_sort_scarecrow(n, k, arr):
        result = 'Yes'
    else:
        result = 'No'

    with open('../txtf/output.txt', "w") as file:
        file.write(result)
