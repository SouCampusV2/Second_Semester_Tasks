import math
import random

# Функция для проверки числа на простоту
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))

# Генерация списка случайных положительных чисел
random_numbers = [random.randint(1, 100) for _ in range(20)]  

# Фильтрация простых чисел из списка
prime_numbers = list(filter(is_prime, random_numbers))

# Вывод
print("Whole array:", random_numbers)
print("Prime numbers:", prime_numbers)
