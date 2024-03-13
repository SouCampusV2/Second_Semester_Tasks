import timeit

# Функция для замера времени удаления элементов из списка
def delete_list(n):
    # Делаем список размером Н
    lst = list(range(n))
    del lst[0]

# Функция для замера времени удаления элементов из словаря
def delete_dict(n):
    # Делаем словарь размером Н
    dct = {i: None for i in range(n)}
    del dct[0]

# Запуск эксперимента для разных размеров списка и словаря, в цикле где перебираются разные размеры обьектов.
for n in [10, 100, 1000, 10000]:
    # Засекаем время с помощью timeit
    # Для себя: в stmt мы передаем кусочек кода который хотим протестировать
    # Для себя: globals = globals() дает доступ ко всем переменым в коде 
    # number = 1000 прикольная штука которая делает действие 1000 раз, и дает усредненный результат.    
    time_list = timeit.timeit(stmt='delete_list(n)', globals=globals(), number=1000)
    time_dict = timeit.timeit(stmt='delete_d    ict(n)', globals=globals(), number=1000)
    print(f"Размер данных: {n}")
    print(f"Время удаления из списка: {time_list:.6f} сек.")
    print(f"Время удаления из словаря: {time_dict:.6f} сек.")
