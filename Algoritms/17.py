def naive_string_matching(T, P):
    # Список для хранения позиций вхождения короткого текста в длинный
    positions = []  
    # Логическое значение для указания успешности поиска
    success = False  

    # Перебор всех возможных начальных позиций в длинном тексте
    for i in range(len(T) - len(P) + 1):
        # Флаг для обозначения совпадения
        match = True  
        # Перебор символов короткого текста
        for j in range(len(P)):
            # Если символы не совпадают, устанавливаем флаг в False и выходим из цикла
            if T[i + j] != P[j]:
                match = False
                break
        # Если все символы совпали, добавляем позицию в список и устанавливаем флаг успешного поиска в True
        if match:
            positions.append(i)
            success = True
    
    return positions, success

# Пример использования функции
T = "ababcabaafbcabaafbc"
P = "abc"
positions, success = naive_string_matching(T, P)
if success:
    print("Короткий текст найден в длинном тексте на позициях:", positions)
else:
    print("Короткий текст не найден в длинном тексте.")
