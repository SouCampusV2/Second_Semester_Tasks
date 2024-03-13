# Первый урок, обозриваем классы, хотя я уже с ними довольно хорошо знаком. Самый простой и стандартный пример,
# это машина, и ее некие свойства. Суть задания в том, чтобы переписать уже существующие методы
# на свои. И делать какое либо сравнение.
class Car:
    def __init__(self, manaf, color, weight):
        # Создаем конструктор с аргументами/свойствами.
        self.manaf = manaf
        self.color = color
       
        # Небольшая проверка, вес не может быть отрицательным.
        if weight > 0:
            self.weight = weight
        # В ином случае мы получим сообщение о том, что вес неправильный.
        else:
            print("Weight must be positive!")
            self.weight = 0

    # Данная функция просто выводит определенный обьект класса
    def __str__(self):
        print("Manaf:", self.manaf, "\nColor:", self.color, "\nWeight:", self.weight)

    # Данная функция сравнивает два свойства первого и второго обьекта класса(Машины). 
    def __eq__(self, a):

        return((a.manaf == self.manaf)and(a.color == self.color))
    # Данная функция сравнивает только одно свойство - вес. 
    def __ge__(self, a):

        return((self.weight) == (a.weight))

# Создаем обьекты класса Машина
m = Car("Mersedes", "Blue", 1600)
b = Car("BMW", "Red", 1400)
a = Car("Audi", "Gray", 1500)

# Выполняем определенные действия использую переписанные методы.
print(m == a)
print(m == b)
print(m >= a)
print(m >= b)



