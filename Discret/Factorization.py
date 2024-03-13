def sieve_of_eratosthenes(limit):
    # Возвращает список всех простых чисел до указанного предела 'limit'.
    primes = []
    # В этом списке будут храниться логические значения, определяющие, является ли число простым.
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми числами

    # Это цикл for, который перебирает числа от 2 до корня квадратного из limit. 
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            # Добавляем все простые числа
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)

    return primes

def prime_factors(n):
    # Возвращает список простых множителей числа n.
    factors = []
    primes = sieve_of_eratosthenes(int(n**0.5) + 1)
    
    for prime in primes:
        # Делится ли число н на какое-то простое число без остатка
        while n % prime == 0:
            factors.append(prime)
            n //= prime
        if n == 1:
            break

    if n > 1:
        factors.append(n)

    return factors

number = int(input("Введите число для факторизации: "))
factors = prime_factors(number)
print("Простые множители числа", number, ":", factors)
