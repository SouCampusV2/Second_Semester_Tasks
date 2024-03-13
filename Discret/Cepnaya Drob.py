def continued_fraction(a, b):
    # Создаем пустой список для хранения компонентов цепной дроби
    result = []  
    while b != 0:
        # Добавляем целую часть от деления числителя на знаменатель
        result.append(a // b)  
        print("Целая часть:", a // b)
        print("Остаток:", a % b)
        print("Дробная часть:", b)
        # Обновляем числитель и знаменатель для следующей итерации
        a, b = b, a % b  
    return result

numerator = int(input("Введите первое число: "))
denominator = int(input("Введите второе число: "))

result = continued_fraction(numerator, denominator)
print("Цепная дробь:", result)
