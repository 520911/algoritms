# Сортировка Хоара

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sort(array, fst, lst):
    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort(array, fst, j)
    quick_sort(array, i, lst)


quick_sort(array, 0, len(array) - 1)
print(array)
