import itertools
import math

# Функция для вычисления расстояния между двумя точками
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Функция для вычисления общей длины маршрута
def total_distance(route, points):
    total = 0
    for i in range(len(route) - 1):
        total += distance(points[route[i]], points[route[i+1]])
    # Учитываем переход к начальной точке
    total += distance(points[route[-1]], points[route[0]])  
    return total

# Функция для нахождения кратчайшего маршрута методом полного перебора
def brute_force_tsp(points):
    num_points = len(points)
    best_route = None
    min_distance = float('inf')
    for route in itertools.permutations(range(num_points)):
        dist = total_distance(route, points)
        if dist < min_distance:
            min_distance = dist
            best_route = route
    return best_route, min_distance

# Точки на плоскости (координаты)
points = [(0, 0), (1, 2), (3, 1), (2, 3), (10,10), (1, 1)]

# Находим кратчайший маршрут методом полного перебора
best_route, min_distance = brute_force_tsp(points)

# Выводим результаты
print("Кратчайший маршрут:", best_route)
print("Длина кратчайшего маршрута:", min_distance)
