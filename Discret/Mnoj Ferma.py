import random

def mod_exp(base, exponent, modulus):
    # Результат - для хранения степени.
    result = 1
    base %= modulus
    while exponent > 0:
        # Четное или не четное.
        if exponent % 2 == 1:
            # Возведения в степень по модулю.
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

# n - число, которое нужно проверить на простоту, и k (по умолчанию 5) - количество случайных тестов для увеличения надежности.
def fermat_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Проверяем с рандомными числами н на простоту
    for _ in range(k):
        a = random.randint(2, n - 1)
        if mod_exp(a, n - 1, n) != 1:
            return False
    return True

# Пример использования:
number = int(input("Введите число для проверки на простоту: "))
if fermat_test(number):
    print(number, "простое числом.")
else:
    print(number, "не простое число.")
