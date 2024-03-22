import math

# Функция суммы двух чисел
def sum(x, y):
    return x + y

# Функция минимума двух чисел
def mini(x, y):
    return min(x, y)

# Функция максимума двух чисел
def maxi(x, y):
    return max(x, y)

# Функция нахождения наименьшего общего кратного
def lcmu(x, y):
    return abs(x) * abs(y) // math.gcd(abs(x), abs(y))

# Функция нахождения наибольшего общего делителя
def gcdi(x, y):
    return abs(math.gcd(x, y))

# Функция операции над массивом с использованием заданной функции и начального значения
def oper_array(fct, arr, init):
    result = []
    accumulator = init
    for i in arr:
        accumulator = fct(accumulator, i)
        result.append(accumulator)
    return result

# Юзаем всё что выше
a = [18, 69, -90, -78, 65, 40]
print("oper_array(gcd, a, a[0]):", oper_array(gcdi, a, a[0]))
print("oper_array(lcm, a, a[0]):", oper_array(lcmu, a, a[0]))
print("oper_array(sum, a, 0):", oper_array(sum, a, 0))
print("oper_array(min, a, a[0]):", oper_array(mini, a, a[0]))
print("oper_array(max, a, a[0]):", oper_array(maxi, a, a[0]))
