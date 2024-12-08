def count_segments_containing_points(s, p, segments, points):
    events = []
    # Добавляем события начала и конца отрезков
    for a, b in segments:
        events.append((a, "start"))
        events.append((b + 1, "end"))

    # Добавляем события точек
    for i, x in enumerate(points):
        events.append((x, "point", i))

    # Сортируем события
    events.sort(key=lambda x: (x[0], x[1] == "point", x[1] == "end"))

    # Результаты и активные отрезки
    active_segments = 0
    result = [0] * p

    for event in events:
        if event[1] == "start":
            active_segments += 1
        elif event[1] == "end":
            active_segments -= 1
        else:  # Точка
            _, _, index = event
            result[index] = active_segments

    return result



if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        s, p = map(int, file.readline().strip().split())
        segments = [tuple(map(int, file.readline().strip().split())) for _ in range(s)]
        points = list(map(int, file.readline().strip().split()))

    result = count_segments_containing_points(s, p, segments, points)


    with open("../txtf/output.txt", "w") as file:
        file.write(" ".join(map(str, result)))