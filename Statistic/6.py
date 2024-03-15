def k_means_clustering(points, k, max_iterations):
    # Инициализация центров кластеров
    min_x = min(points)
    max_x = max(points)
    centers = [min_x + i * (max_x - min_x) / (k - 1) for i in range(k)]
    
    for _ in range(max_iterations):
        # Шаг 2: Приписываем точки к ближайшим центрам кластеров
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [abs(point - center) for center in centers]
            closest_cluster = distances.index(min(distances))
            clusters[closest_cluster].append(point)
        
        # Шаг 3: Перевычисляем координаты центров кластеров
        new_centers = [sum(cluster) / len(cluster) if cluster else center for cluster, center in zip(clusters, centers)]
        
        # Проверка на сходимость
        if new_centers == centers:
            break
        
        centers = new_centers
    
    # Формирование списка кластерной принадлежности точек
    cluster_membership = []
    for point in points:
        distances = [abs(point - center) for center in centers]
        closest_cluster = distances.index(min(distances))
        cluster_membership.append(closest_cluster)
    
    return cluster_membership, centers

# Пример использования:
points = [1, 2, 3, 6, 7, 8, 10, 12, 14, 15]
k = 3
max_iterations = 100

cluster_membership, centers = k_means_clustering(points, k, max_iterations)
print("Кластерная принадлежность:", cluster_membership)
print("Координаты центров кластеров:", centers)
