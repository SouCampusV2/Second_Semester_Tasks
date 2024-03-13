def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

nod = gcd(a, b)
nok = lcm(a, b)

print("Наибольший общий делитель (НОД):", nod)
print("Наименьшее общее кратное (НОК):", nok)

