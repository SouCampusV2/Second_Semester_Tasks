import time
import random

# Бульбашка сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Генерируем рандомный массив на 1000 элементов
def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Проверка и счет скорости сортировок
def test_sorting_algorithm(algorithm, data_size):
    data = generate_random_array(data_size)
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Тестируем производительность сортировки пузырьком
bubble_sort_time = test_sorting_algorithm(bubble_sort, 1000)
print("Сортировка бульбашкой на 1000 элементов:", bubble_sort_time)

# Тестируем производительность быстрой сортировки
quick_sort_time = test_sorting_algorithm(quick_sort, 1000)
print("Быстрая сортировка на 1000 элементов:", quick_sort_time)
