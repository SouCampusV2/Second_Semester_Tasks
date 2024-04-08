import math

def is_prime(n):
    # Проверяет, является ли число n простым.
    if n < 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Перебор делителей от 3 до корня из n с шагом 2
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

# Пример использования:
while True:
    number = int(input("Введите число для проверки на простоту: "))
    if is_prime(number):
        print(number, "является простым числом.")
    else:
        print(number, "не является простым числом.")
