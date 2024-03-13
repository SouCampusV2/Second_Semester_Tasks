# Один из классических примеров первых работ с классами. 
# Герой со своими свойствами и методами атака, лечение и в дополнение отравление.
class Hero:
    def __init__(self, name, damage, health):
        # Создаем конструктор с аргументами/свойствами и своей небольшой логикой.
        self.name = name
        if damage > 0:
            self.damage = damage
        else:
            print("Weight must be positive!")
            self.damage = 0
        if health > 0:
            self.health = health
        else:
            health = 100 

    # Метод сеттер, по условию задания.    
    def set_damage(self, damage):
        if damage > 0:
            self.damage = damage

    # Метод удар.
    def hit(self, other):
        if isinstance(other, Hero):
            other.health = other.health - self.damage

    # Метод лечение.
    def heal(self, num):
        self.health = self.health + num
        
    # Метод отравление.
    def weakness(self, other):
        other.set_damage(other.damage - self.damage)

# Создаем обьекты класса Герой
hero1 = Hero("xxx", 10, 150)
hero2 = Hero("zxcrused", 5, 200)

# Выполняем действия и проверяем.
hero1.hit(hero2)
print(hero2.health)
hero1.weakness(hero2)
