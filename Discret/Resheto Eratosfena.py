def sieve_of_eratosthenes(n):
    # Возвращает список всех простых чисел до n с помощью решета Эратосфена.
    if n <= 1:
        return []

    # Создаём список, заполненный значениями True
    sieve = [True] * (n + 1)  
    # 0 и 1 не являются простыми числами
    sieve[0] = sieve[1] = False  

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                # Вычёркиваем все кратные i
                sieve[j] = False  
    # Формируем список простых чисел
    primes = [i for i in range(2, n + 1) if sieve[i]]  
    return primes

# Пример использования:
upper_bound = int(input("Введите верхнюю границу диапазона поиска простых чисел: "))
prime_numbers = sieve_of_eratosthenes(upper_bound)
print("Простые числа в диапазоне до", upper_bound, ":", prime_numbers)
