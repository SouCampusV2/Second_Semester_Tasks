import random

# Функция для вычисления начальных и центральных моментов
def compute_moments(a, b, n):
    moments = [0] * 4
    for _ in range(n):
        x = random.uniform(a, b)
        moments[0] += x
        moments[1] += (x - (a + b) / 2) ** 2
        moments[2] += (x - (a + b) / 2) ** 3
        moments[3] += (x - (a + b) / 2) ** 4
    moments = [moment / n for moment in moments]
    return moments

# Вычисление начальных и центральных моментов по формулам
def theoretical_moments(a, b):
    mean = (a + b) / 2
    variance = ((b - a) ** 2) / 12
    skewness = 0
    kurtosis = -6 / 5
    return mean, variance, skewness, kurtosis

# Параметры равномерного распределения
a = 0
b = 1

# Количество случайных чисел
n = 10**6

# Вычисление моментов программно
computed_moments = compute_moments(a, b, n)

# Вычисление теоретических моментов
theoretical_moments = theoretical_moments(a, b)

# Вывод результатов
print("Вычисленные программно моменты:")
print("Mean:", computed_moments[0])
print("Variance:", computed_moments[1])
print("Skewness:", computed_moments[2])
print("Kurtosis:", computed_moments[3])

print("\nТеоретические значения моментов:")
print("Mean:", theoretical_moments[0])
print("Variance:", theoretical_moments[1])
print("Skewness:", theoretical_moments[2])
print("Kurtosis:", theoretical_moments[3])
