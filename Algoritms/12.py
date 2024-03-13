import time
import random

# Функция для проведения эксперимента
def experiment(size):
    # Создаем пустой словарь
    dictionary = {}
    
    # Замеряем время для операции записи в словарь
    start_time = time.time()
    for i in range(size):
        dictionary[i] = i
    end_time = time.time()
    write_time = end_time - start_time
    
    # Замеряем время для операции чтения из словаря
    start_time = time.time()
    for i in range(size):
        value = dictionary[i]
    end_time = time.time()
    read_time = end_time - start_time
    
    return write_time, read_time

# Размер словаря (количество элементов)
size = 100000

# Проводим эксперимент
write_time, read_time = experiment(size)

# Выводим результаты
print(f"Запись {size} элементов в словарь заняла {write_time} секунд.")
print(f"Чтение {size} элементов из словаря заняло {read_time} секунд.")
