import os

def calculate_h_index(citations):
    # Сортируем массив в порядке убывания
    citations.sort(reverse=True)
    # Определяем h-индекс
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index


if __name__ == "__main__":
    input_file = os.path.abspath('lab3/task5/txtf/input.txt')
    output_file = os.path.abspath('lab3/task5/txtf/output.txt')

    with open(input_file, "r") as file:
        citations = list(map(int, file.readline().strip().replace(',', ' ').split()))

    result = calculate_h_index(citations)

    with open(output_file, "w") as file:
        file.write(str(result))