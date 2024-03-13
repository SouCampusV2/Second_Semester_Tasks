def nand(a, b):
    return not (a and b)

# Создание таблицы истинности для Шеффера
print("Таблица истинности для Шеффера:")
print("| A | B | (A, B) |")
print("|---|---|--------|")
# Мы перебираем а и б между Тру и фалс. И если они будут оба 1, тобишь тру, тогда результат тоже Тру или же 1
for a in [False, True]:
    for b in [False, True]:
        result = nand(a, b)
        print(f"| {int(a)} | {int(b)} | {int(result)} |")