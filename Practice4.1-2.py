import random
import time

# Бульбашка сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

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

def time_func(fn, *args, rep=1, **kwargs):
    start_time = time.time()
    print("Size = ", len(*args), "time: ")
    fn(*args)
    end_time = time.time()
    print(end_time - start_time)

print("Quick sort.")
time_func(quick_sort, generate_random_array(100))
time_func(quick_sort, generate_random_array(1000))
time_func(quick_sort, generate_random_array(10000))
print("Bubble sort.")
time_func(bubble_sort, generate_random_array(100))
time_func(bubble_sort, generate_random_array(1000))
time_func(bubble_sort, generate_random_array(10000))

# def time_func(fn, *args, rep=1, **kwargs):
#     start_time = time.time()
#     fn((*args, kwargs) * rep)
#     end_time = time.time()
#     print(end_time - start_time)

# time_func(print, 1, 2, 3, rep = 3, a = "ds", b = "dasda")