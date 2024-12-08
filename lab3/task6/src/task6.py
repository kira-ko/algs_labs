import os
from lab3.task1.src.task1 import randomized_quick_sort

def sum_of_every_tenth_product(array1, array2):
    product_list = []
    for b in array2:
        for a in array1:
            product_list.append(a * b)

    randomized_quick_sort(product_list, 0, len(product_list) - 1)
    result = sum(product_list[i] for i in range(0, len(product_list), 10))

    return result

if __name__ == "__main__":
    input_file = os.path.abspath('lab3/task1/txtf/input.txt')
    output_file = os.path.abspath('lab3/task1/txtf/output.txt')

    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        A = list(map(int, f.readline().split()))
        B  = list(map(int, f.readline().split()))

    result = sum_of_every_tenth_product(A, B)

    with open(output_file, 'w') as f:
        f.write(str(result) + '\n')