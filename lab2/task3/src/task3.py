'''Число инверсий'''
def inv_count(array, copy_array, left, middle, right):
    i = left
    j = middle + 1
    k = left
    cnt = 0

    while i <= middle and j <= right:
        if array[i] <= array[j]:
            copy_array[k] = array[i]
            i += 1
        else:
            copy_array[k] = array[j]
            cnt += (middle - i + 1)
            j += 1
        k += 1

    while i <= middle:
        copy_array[k] = array[i]
        i += 1
        k += 1

    while j <= right:
        copy_array[k] = array[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        array[i] = copy_array[i]

    return cnt


def inversions_numbers(array, copy_array, left, right):
    if len(copy_array) < len(array):
        raise ValueError("The Aarray is too small to sort.")

    cnt = 0
    if left < right:
        middle = (left + right) // 2

        cnt += inversions_numbers(array, copy_array, left, middle)
        cnt += inversions_numbers(array, copy_array, middle + 1, right)
        cnt += inv_count(array, copy_array, left, middle, right)

    return cnt


