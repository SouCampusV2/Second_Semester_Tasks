import random

def play_game():
    # Инициализация переменных для подсчета верных и общего числа ответов
    correct_guesses = 0
    total_guesses = 0

    # Цикл игры, который продолжается, пока игрок не решит закончить
    while True:
        # Запрос прогноза у игрока
        prediction = input("Чет (2) или Нечет (1)? Введите ваш прогноз: ")
        # Проверка корректности введенного прогноза
        if prediction.lower() not in ['чет', 'нечет', '2', '1']:
            print("Пожалуйста, введите 'Чет' или 'Нечет' или '2' или '1'.")
            continue

        # Преобразование прогноза игрока в численное значение
        user_prediction = 'чет' if prediction.lower() in ['чет', '2'] else 'нечет'
        # Генерация случайного числа от 1 до 6 (бросок кубика)
        computer_number = random.randint(1, 6)

        # Вывод сгенерированного числа
        print("Выпало число:", computer_number)

        # Проверка совпадения прогноза игрока с результатом броска кубика
        if (computer_number % 2 == 0 and user_prediction == 'чет') or (computer_number % 2 != 0 and user_prediction == 'нечет'):
            print("Верно!")
            correct_guesses += 1
        else:
            print("Неверно!")

        # Увеличение счетчика общего числа ответов
        total_guesses += 1

        # Запрос желания игрока продолжить игру или завершить
        play_again = input("Продолжить еще раз? (Да/Нет): ")
        if play_again.lower() != 'да':
            break
        elif play_again.lower() == 'стоп':
            break

    # Возврат количества верных и общего числа ответов
    return correct_guesses, total_guesses

def calculate_relative_frequency(total_rolls):
    # Генерация списка случайных чисел при бросках кубика
    rolls = [random.randint(1, 6) for _ in range(total_rolls)]
    # Подсчет количества выпадений каждого числа от 1 до 6
    frequency = {i: rolls.count(i) for i in range(1, 7)}
    return frequency

# Игра
print("Добро пожаловать в игру 'Чет или Нечет'!")
correct, total = play_game()
print("Игра завершена.")
print("Количество верных ответов:", correct)
print("Количество неверных ответов:", total - correct)

# Подсчет относительной частоты бросаний кубика
print("\nПодсчет относительной частоты бросаний кубика:")
print("При 100 бросаниях:")
frequency_100 = calculate_relative_frequency(100)
print(frequency_100)
print("При 1000 бросаниях:")
frequency_1000 = calculate_relative_frequency(1000)
print(frequency_1000)
