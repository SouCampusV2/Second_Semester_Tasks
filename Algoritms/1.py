def find_extreme_element(arr, key):

    # Инициализация переменной для хранения значения наименьшего/наибольшего элемента
    extreme_value = None  
    # Инициализация списка для хранения индексов элементов с наименьшим/наибольшим значением
    extreme_indices = []  

    # Находим наименьший элемент списка
    if key == 'min':
        extreme_value = min(arr)  
    # Находим наибольший элемент списка
    elif key == 'max':
        extreme_value = max(arr)  

    # Проходим по списку и записываем индексы элементов с наименьшим/наибольшим значением
    for i, val in enumerate(arr):
        if val == extreme_value:
            extreme_indices.append(i)
    # Возвращаем значение наименьшего/наибольшего элемента и список его индексов
    return extreme_value, extreme_indices  

arr = [78, 92, 15, 166, 21, 97, 139, 24, 12, 69, 196, 148, 74, 95, 48, 153, 115, 157, 120, 94, 127, 63, 70, 43, 115, 119, 101, 131, 69, 200, 21, 88, 50, 176, 189, 152, 158, 182, 157, 198, 21, 100, 193, 32, 194, 178, 123, 159, 18, 126, 108, 147, 3, 94, 32, 176, 14, 69, 40, 102, 182, 123, 76, 81, 177, 25, 148, 15, 161, 185, 184, 95, 93, 99, 133, 174, 8, 14, 128, 172, 17, 90, 28, 147, 18, 47, 79, 111, 197, 69, 166, 192, 143, 92, 67, 79, 71, 159, 74, 194, 1, 80, 63, 119, 195, 78, 24, 131, 194, 184, 26, 200, 161, 193, 42, 116, 150, 52, 200, 134, 47, 67, 71, 54, 131, 198, 61, 151, 142, 171, 114, 187, 143, 150, 18, 155, 109, 30, 106, 83, 187, 41, 78, 109, 122, 102, 12, 165, 34, 114, 16, 111, 66, 56, 115, 155, 167, 178, 60, 177, 47, 167, 144, 191, 3, 51, 1, 78, 22, 32, 149, 38, 188, 42, 146, 187, 132, 25, 96, 43, 3, 199, 183, 45, 171, 57, 82, 163, 13, 11, 62, 162, 28, 22, 46, 132, 50, 83, 138, 43, 13, 15, 144, 124, 140, 172, 174, 14, 117, 26, 121, 60, 148, 96, 180, 15, 1, 38, 88, 41, 77, 28, 108, 104, 49, 198, 3, 173, 74, 80, 196, 80, 148, 163, 73, 121, 161, 142, 189, 30, 110, 68, 127, 70, 193, 180, 162, 131, 153, 198, 56, 36, 141, 187, 126, 121, 93, 7, 100, 96, 20, 26, 99, 87, 143, 6, 140, 44, 6, 32, 5, 71, 85, 65, 190, 5, 42, 22, 138, 184, 148, 91, 125, 124, 191, 29, 134, 84, 83, 108, 55, 148, 104, 107, 195, 105, 141, 23, 62, 129, 34, 140, 200, 43, 11, 139, 152, 128, 198, 30, 150, 4, 50, 32, 24, 109, 47, 38, 7, 154, 96, 17, 44, 24, 159, 2, 57, 69, 178, 35, 200, 154, 162, 92, 42, 62, 125, 153, 186, 22, 125, 107, 183, 169, 133, 159, 121, 91, 22, 50, 11, 185, 86, 164, 156, 49, 30, 146, 170, 47, 161, 160, 99, 179, 156, 124, 114, 168, 52, 186, 187, 103, 120, 36, 124, 149, 93, 49, 189, 90, 198, 197, 22, 51, 163, 190, 177, 2, 97, 146, 91, 94, 99, 104, 16, 79, 179, 59, 23, 49, 172, 106, 132, 15, 119, 107, 7, 60, 117, 53, 137, 84, 58, 79, 77, 111, 118, 90, 141, 130, 61, 65, 25, 60, 38, 167, 187, 173, 200, 88, 1, 26, 36, 32, 110, 59, 122, 162, 19, 56, 96, 40, 42, 61, 16, 143, 135, 33, 18, 20, 17, 167, 97, 41, 160, 176, 108, 36, 33, 199, 104, 76, 146, 18, 97, 50, 159, 174, 24, 12, 199, 101, 167, 178, 86, 184, 109, 196, 42, 97, 149, 50, 99, 169, 23, 3, 122, 114, 12, 96, 41, 81, 38, 80, 162, 149, 146, 112, 63, 168, 131, 55, 64, 61, 63, 97, 167, 93, 1, 154, 157, 12, 184, 46, 7, 142, 109, 35, 178, 151, 127, 40, 63, 90, 196, 183, 68, 131, 113, 106, 21, 21, 94, 28, 173, 25, 106, 152, 168, 36, 100, 131, 81, 142, 49, 65, 187, 118, 24, 177, 144, 34, 138, 26, 2, 121, 138, 154, 1, 154, 158, 32, 50, 80, 69, 170, 120, 128, 174, 17, 166, 88, 157, 96, 131, 176, 148, 142, 109, 132, 154, 191, 74, 200, 123, 115, 161, 123, 10, 92, 84, 166, 166, 195, 5, 69, 19, 168, 78, 187, 58, 72, 43, 6, 111, 170, 48, 182, 74, 67, 72, 135, 145, 110, 78, 129, 128, 45, 172, 81, 176, 21, 19, 9, 167, 154, 172, 162, 159, 68, 191, 40, 102, 4, 2, 122, 133, 113, 4, 60, 115, 99, 85, 138, 109, 28, 18, 23, 85, 13, 15, 192, 193, 83, 137, 172, 83, 85, 74, 55, 197, 200, 162, 159, 175, 55, 3, 35, 30, 120, 99, 147, 179, 133, 10, 85, 194, 157, 27, 109, 68, 119, 21, 95, 117, 38, 47, 52, 77, 195, 10, 108, 138, 143, 96, 35, 68, 156, 14, 61, 198, 109, 46, 17, 3, 109, 158, 193, 60, 191, 135, 87, 108, 167, 143, 197, 190, 159, 116, 161, 70, 194, 200, 77, 101, 73, 133, 50, 133, 130, 100, 7, 12, 84, 131, 10, 45, 13, 7, 162, 55, 49, 76, 116, 3, 66, 171, 174, 33, 88, 116, 62, 95, 155, 117, 171, 41, 74, 71, 52, 189, 106, 169, 182, 81, 2, 177, 46, 146, 147, 184, 5, 24, 161, 28, 88, 13, 21, 79, 141, 107, 143, 1, 198, 114, 106, 107, 30, 92, 108, 94, 42, 91, 15, 3, 196, 150, 125, 68, 119, 188, 167, 8, 116, 32, 135, 59, 90, 105, 178, 26, 31, 196, 99, 158, 57, 21, 170, 147, 100, 45, 6, 44, 28, 125, 3, 199, 175, 200, 95, 137, 196, 45, 170, 191, 9, 158, 179, 159, 161, 59, 180, 5, 6, 167, 125, 172, 104, 25, 17, 14, 179, 190, 166, 146, 80, 147, 5, 72, 6, 5, 80, 99, 95, 42, 136, 11, 6, 176, 57, 159, 28, 83, 89, 144, 197, 41, 113, 147, 125, 136, 47, 186, 10, 147, 5, 104, 12, 101, 135, 44, 108, 181, 94, 194, 117, 9, 95, 119, 150, 26, 66, 10, 78, 78, 33, 32, 23, 116, 138, 81, 194, 173, 188, 19, 77, 85, 188, 182, 199, 26, 33, 36, 159, 4, 91, 170, 73, 192, 98, 60, 104, 92, 5, 157, 130, 75, 11, 43, 180, 83, 30, 161, 40, 145, 69, 49, 132, 103, 53, 142, 54, 105, 184, 167, 172, 176, 23, 106, 173, 174, 122, 52, 81, 85, 25, 68, 46, 143, 195, 51, 112, 176, 10, 103, 21, 172, 177, 63, 76, 137, 199, 171, 55, 15, 62, 23, 57, 28, 48, 197, 43, 53, 1, 108, 3, 120, 160, 198, 3]

# Вызываем функцию
extreme_value, extreme_indices = find_extreme_element(arr, "min")

# Выводим результаты
if len(extreme_indices) > 1:
    print(f"Наименьшие элементы: {extreme_value} с индексами {extreme_indices}")
else:
    print(f"Наименьший элемент: {extreme_value} с индексом {extreme_indices[0]}")

extreme_value, extreme_indices = find_extreme_element(arr, "max")

# Выводим результаты
if len(extreme_indices) > 1:
    print(f"Наибольшие элементы: {extreme_value} с индексами {extreme_indices}")
else:
    print(f"Наибольший элемент: {extreme_value} с индексом {extreme_indices[0]}")