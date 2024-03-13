# Проверяет, можно ли заданное множество разбить на два подмножества с равными суммами элементов.
def can_split_equal_sum_subsets(numbers):
     # Нужно чтобы понимать число парное вообще или нет, можно ли его поделить на два подмножества
    total_sum = sum(numbers)

    # Проверяем, можно ли разделить множество на два подмножества
    if total_sum % 2 != 0:
        # Невозможно разделить на два подмножества с равными суммами, тогда возвращаем фалс - неудача
        return False, [], []  
    target_sum = total_sum // 2

    # Функция для поиска подмножества с суммой, равной target_sum
    def backtrack(start_index, curr_sum, curr_subset):
        # Если с помощью перебора мы дошли до суммы, то все супер, тру
        if curr_sum == target_sum:
            return True, curr_subset
        # С помощи рекурсии перебираем числа далее(подсмотрел в интернете)
        for i in range(start_index, len(numbers)):
            if curr_sum + numbers[i] <= target_sum:
                result, subset = backtrack(i + 1, curr_sum + numbers[i], curr_subset + [numbers[i]])
                if result:
                    return True, subset

        return False, []

    # Начинаем рекурсивный поиск
    result, subset1 = backtrack(0, 0, [])

    # Если удалось найти первое подмножество, создаем второе по индексам
    if result:
        # Индексы использованных элементов из первого подмножества(тоже в интернете нашел и немного переделал)
        used_indices = {numbers.index(num) for num in subset1}  
        subset2 = [num for i, num in enumerate(numbers) if i not in used_indices]
        if sum(subset1) == sum(subset2):
            return True, subset1, subset2
        else:
            return False, [], []
    else:
        return False, [], []

# Пример использования функции:
numbers = [1, 2, 3, 4, 5, 6, 7]
# Сортировка нужна чтобы просто работал метод для определения подмножеств с равной суммой
numbers.sort()
result, subset1, subset2 = can_split_equal_sum_subsets(numbers)
if result:
    print("Первое подмножество:", subset1)
    print("Второе подмножество:", subset2)
else:
    print("Невозможно разделить множество на два подмножества с равными суммами.")
