def binary_search(arr, target):
    """
    Функция для бинарного поиска в отсортированном списке.

    Аргументы:
    arr (list): Отсортированный список чисел.
    target (int): Искомое число.

    Возвращает:
    int: Индекс искомого числа в списке, если найдено, иначе -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования
arr = [2, 5, 10, 15, 18, 20, 25, 30, 35, 40, 45]
target = 18

result = binary_search(arr, target)
if result != -1:
    print(f"Число {target} найдено в списке на индексе {result}.")
else:
    print(f"Число {target} не найдено в списке.")
