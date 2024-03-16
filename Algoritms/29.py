def calculate_rank(num, nums):
    # Функция для вычисления ранга числа.
    # Считаем количество чисел в списке nums, которые меньше num
    less_than_num = sum(1 for x in nums if x < num)
    
    # Считаем количество чисел в списке nums, равных num
    equal_to_num = nums.count(num)
    
    # Расчет ранга по формуле, описанной в задаче
    return less_than_num + (equal_to_num - 1) / 2 + 1

def spearman_rank_correlation(x, y):
    # Возвращает коэффициент ранговой корреляции Спирмена для списков x и y.
    # Проверяем, что списки имеют одинаковую длину
    if len(x) != len(y):
        raise ValueError("Lists must be of equal length")
    
    # Длина списка
    n = len(x)
    
    # Вычисляем ранги для каждой переменной
    rank_x = [calculate_rank(x[i], x) for i in range(n)]
    rank_y = [calculate_rank(y[i], y) for i in range(n)]
    
    # Вычисляем разницу в рангах и квадраты этой разницы
    rank_diff_squared = sum((rank_x[i] - rank_y[i]) ** 2 for i in range(n))
    
    # Вычисляем коэффициент ранговой корреляции Спирмена
    correlation = 1 - (6 * rank_diff_squared) / (n * (n ** 2 - 1))
    
    return correlation

# Пример использования
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
correlation = spearman_rank_correlation(x, y)
print("Коэффициент ранговой корреляции Спирмена:", correlation)
