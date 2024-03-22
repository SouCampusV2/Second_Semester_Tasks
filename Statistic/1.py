# Примеяание, очень не уверен что работает правильно

import random  
from collections import Counter  

# Функция для нахождения минимального значения в наборе данных
def find_min(data):
    return min(data)

# Функция для нахождения максимального значения в наборе данных
def find_max(data):
    return max(data)

# Функция для вычисления вариационного размаха
def calculate_range(min_value, max_value):
    return max_value - min_value

# Функция для построения дискретного вариационного ряда
def construct_discrete_variational_series(data):
    return sorted(data)

# Функция для построения интервального вариационного ряда
def construct_interval_variational_series(data, num_intervals):
    # Нахождение мин макс значения в данных
    min_value = min(data)  
    max_value = max(data)
    # Расчет размера интервала
    interval_size = (max_value - min_value) / num_intervals  
    # Пустой список для хранения интервалов
    intervals = []  
    # Инициализация текущего минимального значения
    current_min = min_value  
    # Цикл для создания интервалов
    for i in range(num_intervals):
        # Добавление интервала в список
        intervals.append((current_min, current_min + interval_size))  
        # Переход к следующему интервалу
        current_min += interval_size  
    # Корректировка последнего интервала
    intervals[-1] = (intervals[-1][0], max_value)  
    # Пустой список для вариационного ряда
    series = []  
    # Цикл для присвоения элементов к интервалам
    for item in data:
        for interval in intervals:
            # Проверка, в какой интервал попадает элемент
            if interval[0] <= item < interval[1]:  
                # Добавление интервала в вариационный ряд
                series.append(interval)  
                break
    return series

# Функция для вычисления начальных моментов порядка order
def calculate_moments(data, order):
    # Получение количества элементов в данных
    n = len(data)  
    # Вычисление среднего значения
    mean = sum(data) / n  
    # Вычисление момента порядка order
    moments = sum((x - mean) ** order for x in data) / n  
    return moments

# Функция для вычисления центральных моментов порядка order
def calculate_central_moments(data, order):
    # Получение количества элементов в данных
    n = len(data)  
    # Вычисление среднего значения
    mean = sum(data) / n  
    # Вычисление центрального момента порядка order
    central_moments = sum((x - mean) ** order for x in data) / n  
    return central_moments

# Функция для вычисления моды
def calculate_mode(data):
    # Подсчет количества вхождений каждого элемента в данные
    count = Counter(data)  
    # Нахождение элемента с наибольшим количеством вхождений
    mode = count.most_common(1)[0][0]  
    return mode

# Функция для вычисления медианы
def calculate_median(data):
    # Получение количества элементов в данных
    n = len(data)  
    # Сортировка данных по возрастанию
    sorted_data = sorted(data)  
    # Проверка на четность количества элементов
    if n % 2 == 0:  
        # Вычисление медианы для четного количества элементов
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2  
    else:
        # Вычисление медианы для нечетного количества элементов
        median = sorted_data[n//2]  
    return median

# Функция для вычисления асимметрии
def calculate_skewness(data):
    # Получение количества элементов в данных
    n = len(data)  
    # Вычисление среднего значения
    mean = sum(data) / n  
    # Вычисление дисперсии
    variance = sum((x - mean) ** 2 for x in data) / n  
    # Вычисление асимметрии
    skewness = sum((x - mean) ** 3 for x in data) / (n * variance ** (3 / 2))  
    return skewness

# Функция для вычисления эксцесса
def calculate_kurtosis(data):
    n = len(data)  
    mean = sum(data) / n  
    variance = sum((x - mean) ** 2 for x in data) / n  
    # Вычисление эксцесса
    kurtosis = sum((x - mean) ** 4 for x in data) / (n * variance ** 2) - 3  
    return kurtosis

# Количество случайных чисел
n = 10  
x = [random.randint(0, 10) for i in range(n)]  

# Вычисление статистических характеристик
minimum = find_min(x)
maximum = find_max(x)
range_value = calculate_range(minimum, maximum)
discrete_variational_series = construct_discrete_variational_series(x)
interval_variational_series = construct_interval_variational_series(x, num_intervals=5)
moments_1 = calculate_moments(x, 1)
moments_2 = calculate_moments(x, 2)
moments_3 = calculate_moments(x, 3)
moments_4 = calculate_moments(x, 4)
central_moments_1 = calculate_central_moments(x, 1)
central_moments_2 = calculate_central_moments(x, 2)
central_moments_3 = calculate_central_moments(x, 3)
central_moments_4 = calculate_central_moments(x, 4)
mode = calculate_mode(x)
median = calculate_median(x)
skewness = calculate_skewness(x)
kurtosis = calculate_kurtosis(x)

# Вывод результатов
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Вариационный размах:", range_value)
print("Дискретный вариационный ряд:", discrete_variational_series)
print("Интервальный вариационный ряд:", interval_variational_series)
print("Начальные моменты порядка 1, 2, 3, 4:", moments_1, moments_2, moments_3, moments_4)
print("Центральные моменты порядка 1, 2, 3, 4:", central_moments_1, central_moments_2, central_moments_3, central_moments_4)
print("Мода:", mode)
print("Медиана:", median)
print("Асимметрия:", skewness)
print("Эксцесс:", kurtosis)