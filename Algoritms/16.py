def radix_sort(arr):
    # Создаем 10 цифровых корзин (0-9)
    buckets = [[] for _ in range(10)]

    # Сортируем массив по единицам
    for num in arr:
        digit_val = num % 10
        buckets[digit_val].append(num)
    
    # Собираем числа обратно в исходный массив
    # Эта строка присваивает полученный список обратно переменной arr, 
    # перезаписывая ее. Теперь arr содержит числа, отсортированные в соответствии
    # с текущим разрядом.
    arr = [num for bucket in buckets for num in bucket]
    # Очищаем корзины
    buckets = [[] for _ in range(10)]

    # Сортируем массив по десяткам
    for num in arr:
        digit_val = (num // 10) % 10
        buckets[digit_val].append(num)
    
    # Собираем числа обратно в исходный массив
    arr = [num for bucket in buckets for num in bucket]
    # Очищаем корзины
    buckets = [[] for _ in range(10)]

    # Сортируем массив по сотням
    for num in arr:
        digit_val = (num // 100) % 10
        buckets[digit_val].append(num)

    # Собираем числа обратно в исходный массив
    arr = [num for bucket in buckets for num in bucket]

    return arr

# Пример использования
arr = [170, 454, 775, 900, 802, 244, 254, 666]
sorted_arr = radix_sort(arr)
print("Отсортированный массив:", sorted_arr)
