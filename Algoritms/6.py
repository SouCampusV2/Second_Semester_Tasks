import math

def golden_ratio_search(arr, target):
    n = len(arr)
    # Находим начальные границы
    left, right = 0, n - 1
    
    # Золотое сечение
    phi = (1 + math.sqrt(5)) / 2
    
    # Индексы для деления массива
    x1 = int(right - (right - left) / phi)
    x2 = int(left + (right - left) / phi)
    
    while arr[x1] != target and arr[x2] != target:
        if arr[x1] < target:
            left = x1
            x1 = x2
            x2 = int(left + (right - left) / phi)
        else:
            right = x2
            x2 = x1
            x1 = int(right - (right - left) / phi)
        
        # Проверка на выход за границы массива
        if x1 < left or x2 > right:
            return -1
    
    if arr[x1] == target:
        return x1
    elif arr[x2] == target:
        return x2
    else:
        return -1

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Число которое ищем
target = 7
index = golden_ratio_search(arr, target)
if index != -1:
    print(f"Элемент {target} найден в позиции {index}.")
else:
    print(f"Элемент {target} не найден в массиве.")
