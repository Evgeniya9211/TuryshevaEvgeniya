import random

def sort_by_inserts(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


sequence_numbers_string = input("Введите последовательность чисел через пробел: ")
element = int(input("Введите любое число для поиска его в отсортированном списке: "))

sequence_numbers_list = list(map(int, sequence_numbers_string.split(sep=" ")))

sequence_sorted = sort_by_inserts(sequence_numbers_list)
print("Сортировка списка по возрастанию в нем элементов: ", sequence_sorted)

# запускаем алгоритм на левой и правой границе
element_index = binary_search(sequence_sorted, element, 0, len(sequence_sorted))
print("Индекс элемента, введенного пользователем, в отсортированном массиве: ", element_index)
