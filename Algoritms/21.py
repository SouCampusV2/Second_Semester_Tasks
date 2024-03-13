def get_ratio(item):
    # Вычисляет отношение стоимости к массе предмета.
    # param item - Кортеж (масса, стоимость) предмета.
    # return - Отношение стоимости к массе.
    weight, value = item
    return value / weight

def knapsack_brute_force(items, capacity):
    # Решаем задачу о рюкзаке методом грубой силы.
    # param items - Список кортежей (масса, стоимость) предметов.
    # param capacity - Грузоподъемность рюкзака.
    # return - Максимальная суммарная стоимость предметов, помещенных в рюкзак. 
    n = len(items)
    max_value = 0

    # Генерируем все возможные комбинации предметов
    for i in range(2 ** n):
        total_weight = 0
        total_value = 0
        for j in range(n):
            if (i >> j) & 1:
                total_weight += items[j][0]
                total_value += items[j][1]
                # Если общий вес превышает грузоподъемность, прекращаем итерацию
                if total_weight > capacity:
                    break
        # Обновляем максимальную стоимость, если текущая комбинация удовлетворяет условиям
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value

    return max_value

# Пример использования функции
items = [(2, 3), (3, 4), (4, 5), (1, 6), (1, 7)]  # Пример предметов: (масса, стоимость)
capacity = 10  # Пример грузоподъемности рюкзака

# Сортируем предметы по отношению стоимость/масса
items.sort(key=get_ratio, reverse=True)

max_value = knapsack_brute_force(items, capacity)
print("Максимальная суммарная стоимость предметов в рюкзаке:", max_value)
