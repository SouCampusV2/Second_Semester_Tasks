import random
import time

# Функция сортировки выбором
def selection_sort(arr):
    # Переменные для подсчета количества действий и сравнений
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return comparisons, swaps

# Функция сортировки вставками
def insertion_sort(arr):
    # Переменные для подсчета количества действий и сравнений
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
    return comparisons, swaps

# Создаем список из 500 случайных чисел
arr = [random.randint(0, 1000) for _ in range(500)]

# Копируем список для каждой сортировки, чтобы они работали с одинаковыми данными
arr_selection = arr.copy()
arr_insertion = arr.copy()

# Сортировка выбором и засекаем время
start_time = time.time()
comparisons_selection, swaps_selection = selection_sort(arr_selection)
end_time = time.time()
# Посчитали потраченное время
time_selection = end_time - start_time

# Сортировка вставками и засекаем время
start_time = time.time()
comparisons_insertion, swaps_insertion = insertion_sort(arr_insertion)
end_time = time.time()
# Посчитали потраченное время
time_insertion = end_time - start_time

# Вывод результатов
print("Сортировка выбором:")
print("Количество сравнений:", comparisons_selection)
print("Количество перестановок:", swaps_selection)
print("Время выполнения:", time_selection, "сек.\n")

print("Сортировка вставками:")
print("Количество сравнений:", comparisons_insertion)
print("Количество перестановок:", swaps_insertion)
print("Время выполнения:", time_insertion, "сек.")
