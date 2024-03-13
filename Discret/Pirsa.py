def nor(a, b):
    return not (a or b)

# Создание таблицы истинности для Шеффера
print("Таблица истинности для Пирса:")
print("| A | B | (A, B) |")
print("|---|---|--------|")
# Мы перебираем а и б между Тру и фалс. И если они будут оба 0, тобишь фалс, тогда результат тоже Тру или же 1
for a in [False, True]:
    for b in [False, True]:
        result = nor(a, b)
        print(f"| {int(a)} | {int(b)} | {int(result)} |")