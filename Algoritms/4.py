import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, target):
    # Бинарный поиск в отсортированном массиве arr.
    # Возвращает индекс элемента, если он найден, иначе возвращает -1.
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test_binary_search(arr, target):
    # Функция для тестирования производительности бинарного поиска.
    # Принимает отсортированный массив и цель поиска,
    # выполняет бинарный поиск цели в массиве
    # и возвращает затраченное на это время.
    
    start_time = time.time()
    # Тайм слип по неизвестной мне причине помогает отобразить время работы, без него будет 0.0
    time.sleep(2)
    result = binary_search(arr, target)
    end_time = time.time()
    print("Массив размером", len(arr), "за время: ", end_time - start_time)
    return end_time - start_time

# Определенная цель поиска
target = 1
# Создание массивов и тестирование производительности для разных размеров массивов
sizes = [1000, 5000, 10000, 20000, 50000]
times = []

for size in sizes:
    data = sorted(random.sample(range(size * 10), size))
    time_taken = test_binary_search(data, target)
    times.append(time_taken)
# Построение графика

plt.plot(sizes, times, marker='o')
plt.title('Зависимость времени выполнения бинарного поиска от количества элементов')
plt.xlabel('Количество элементов')
plt.ylabel('Время выполнения (сек)')
plt.grid(True)
plt.show()
