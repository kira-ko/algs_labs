from lab3.task1.src.task1 import randomized_quick_sort

def sum_of_every_tenth_product(array1, array2):
    product_list = []
    for b in array2:
        for a in array1:
            product_list.append(a * b)

    randomized_quick_sort(product_list, 0, len(product_list) - 1)
    result = sum(product_list[i] for i in range(0, len(product_list), 10))

    return result