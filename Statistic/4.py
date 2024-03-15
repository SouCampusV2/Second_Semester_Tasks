import math

# Функция для вычисления среднего значения
def mean(values):
    return sum(values) / len(values)

# Функция для вычисления стандартного отклонения
def std_deviation(values):
    mean_val = mean(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

# Функция для вычисления коэффициента линейной корреляции Пирсона
def pearson_correlation(x_values, y_values):
    mean_x = mean(x_values)
    mean_y = mean(y_values)
    std_dev_x = std_deviation(x_values)
    std_dev_y = std_deviation(y_values)
    
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, y_values))
    denominator = len(x_values) * std_dev_x * std_dev_y
    
    return numerator / denominator

# Функция для вычисления матрицы коэффициентов корреляций
def correlation_matrix(data):
    num_variables = len(data)
    corr_matrix = [[0] * num_variables for _ in range(num_variables)]
    
    for i in range(num_variables):
        for j in range(num_variables):
            corr_matrix[i][j] = pearson_correlation(data[i], data[j])
    
    return corr_matrix

# Пример использования:
# Данные для тестирования
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 4, 5, 6]
z_values = [3, 4, 5, 6, 7]

# Вычисление коэффициента линейной корреляции Пирсона для двух переменных
correlation_coefficient_xy = pearson_correlation(x_values, y_values)
print("Коэффициент корреляции между x и y:", correlation_coefficient_xy)

# Вычисление матрицы коэффициентов корреляций для трех переменных
data = [x_values, y_values, z_values]
corr_matrix = correlation_matrix(data)
print("\nМатрица коэффициентов корреляций:")
for row in corr_matrix:
    print(row)
