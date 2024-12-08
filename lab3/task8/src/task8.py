import heapq
import math
import os


def k_closest_points_to_origin(n, K, points):
    # Используем кучу для хранения точек с наименьшим расстоянием
    max_heap = []

    for x, y in points:
        # Расстояние до начала координат
        distance = math.sqrt(x ** 2 + y ** 2)
        # Добавляем точку в кучу
        heapq.heappush(max_heap, (-distance, (x, y)))  # Отрицательное расстояние для макс-кучи
        # Если кучи больше K, удаляем самую дальнюю точку
        if len(max_heap) > K:
            heapq.heappop(max_heap)

    # Извлекаем точки из кучи и сортируем их
    closest_points = [point for _, point in max_heap]
    closest_points.sort(key=lambda point: math.sqrt(point[0] ** 2 + point[1] ** 2))

    return closest_points


if __name__ == "__main__":
    input_file = os.path.abspath('lab3/task1/txtf/input.txt')
    output_file = os.path.abspath('lab3/task1/txtf/output.txt')

    with open(input_file, 'r') as file:
        n, K = map(int, file.readline().split())
        points = [tuple(map(int, file.readline().split())) for _ in range(n)]

    result = k_closest_points_to_origin(n, K, points)

    with open(output_file, 'w') as file:
        file.write(str(result) + '\n')
