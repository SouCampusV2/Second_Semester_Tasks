# Функция для вычисления ранга числа
def rank_number(number, sorted_values):
    count_less = sum(1 for value in sorted_values if value < number)
    count_equal = sorted_values.count(number)
    return count_less + (count_equal + 1) / 2

# Функция для вычисления рангов для всего списка
def rank_values(values):
    sorted_values = sorted(values, reverse=True)
    ranks = [rank_number(number, sorted_values) for number in values]
    return ranks

# Функция для вычисления коэффициента корреляции Спирмена
def spearman_correlation(x_values, y_values):
    n = len(x_values)
    rank_x = rank_values(x_values)
    rank_y = rank_values(y_values)
    squared_diff_rank = sum((rank_x[i] - rank_y[i]) ** 2 for i in range(n))
    return 1 - 6 * squared_diff_rank / (n * (n ** 2 - 1))

# Пример использования:
# Данные для тестирования
x_values = [10, 20, 30, 40, 10]
y_values = [4, 15, 25, 35, 45]

# Вычисление коэффициента корреляции Спирмена
correlation = spearman_correlation(x_values, y_values)
print("Коэффициент корреляции Спирмена:", correlation)
