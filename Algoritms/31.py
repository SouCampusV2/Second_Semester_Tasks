# 1 - T(n) = 2 T(n/2) + n^2
# Метод дерева рекурсии:

# На каждом уровне дерева рекурсии рекурсивный вызов делится на две подзадачи размером n/2.
# Затем каждая из этих подзадач делится на две подзадачи размером (n/2)/2 = n/4, и так далее.
# Глубина дерева рекурсии будет log(n) (основание 2).
# На каждом уровне у нас есть 2^k подзадач, каждая из которых требует O(n^2) времени на решение.
# Поэтому на каждом уровне мы тратим O(n^2) времени на решение всех подзадач.
# Метод подстановки:

# Предположим, что T(k) = O(k^2) для всех k < n.
# Подставим это предположение в исходное уравнение: T(n) = 2T(n/2) + n^2.
# Получим: T(n) = 2*(n/2)^2 + n^2 = n^2 + n^2 = 2n^2.
# Таким образом, T(n) = O(n^2).


# 2 - T(n) = 2 T(n/2) + n^3
# Метод дерева рекурсии:

# Аналогично предыдущему случаю, на каждом уровне дерева рекурсии каждая подзадача требует O(n^3) времени на решение.
# Глубина дерева рекурсии также составляет log(n).
# Поэтому на каждом уровне мы тратим O(n^3) времени на решение всех подзадач.
# Метод подстановки:

# Предположим, что T(k) = O(k^3) для всех k < n.
# Подставим это предположение в исходное уравнение: T(n) = 2T(n/2) + n^3.
# Получим: T(n) = 2*(n/2)^3 + n^3 = n^3 + n^3 = 2n^3.
# Таким образом, T(n) = O(n^3).

# 1
def solve_recurrence(T, n):
    if n == 1:
        return 1  # Базовый случай рекурсии
    else:
        # Выводим текущее рекуррентное соотношение
        print(f"Solving T({n}) = 2T({n/2}) + {n}^2")
        # Рекурсивно решаем подзадачу для n/2  
        subproblem = solve_recurrence(T, n//2)  
        # Выводим промежуточные вычисления
        print(f"Solving T({n}) = 2 * T({n/2}) + {n}^2 = 2 * {subproblem} + {n}^2")  
        # Решаем текущую задачу по рекуррентному соотношению
        result = 2 * subproblem + n**2  
        # Выводим результат
        print(f"= {result}\n")  
        return result

# Пример вызова функции для решения рекуррентного соотношения
n = 8
print(f"Solution for T({n}):")
solution = solve_recurrence(None, n)
print(f"T({n}) = {solution}")

#2
def solve_recurrence(T, n):
    if n == 1:
        # Базовый случай рекурсии
        return 1  
    else:
        # Выводим текущее рекуррентное соотношение
        print(f"Solving T({n}) = 2T({n/2}) + {n}^3")  
        # Рекурсивно решаем подзадачу для n/2
        subproblem = solve_recurrence(T, n//2)  
         # Выводим промежуточные вычисления
        print(f"Solving T({n}) = 2 * T({n/2}) + {n}^3 = 2 * {subproblem} + {n}^3") 
        # Решаем текущую задачу по рекуррентному соотношению
        result = 2 * subproblem + n**3
        # Выводим результат
        print(f"= {result}\n")  
        return result

# Пример вызова функции для решения рекуррентного соотношения
n = 8
print(f"Solution for T({n}):")
solution = solve_recurrence(None, n)
print(f"T({n}) = {solution}")
