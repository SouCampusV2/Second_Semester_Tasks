import random
import ctypes
import gc

class Hero:
    def __init__(self, name, damage, health):
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
        self.target = None
    def set_damage(self, damage):
        if damage > 0:
            self.damage = damage

    def set_target(self, target):
        self.target = target

    def __del__(self):
        print(self.name + " died.")

    def hit(self, other):
        self.set_target(other)
        if isinstance(other, Hero):  
            a = random.randint(0, 100)
            other.health = other.health - a
              
    def heal(self, num):
        self.health = self.health + num
        
    def weakness(self, other):
        other.set_damage(other.damage - self.damage)



hero1 = Hero("xxx", 10, 150)
hero2 = Hero("zxcrused", 5, 150)

while(True):
    if(hero2.health > 0):
        hero1.hit(hero2)
        print(hero2.name, hero2.health)
    else:
        hero1 = None
        hero2 = None
        break
    if(hero1.health > 0):
        hero2.hit(hero1)
        print(hero1.name, hero1.health)
    else: 
        hero1 = None
        hero2 = None
        break


print(ctypes.c_long.from_address(id(hero1)).value)
print(ctypes.c_long.from_address(id(hero2)).value)

gc.collect()

print(ctypes.c_long.from_address(id(hero1)).value)
print(ctypes.c_long.from_address(id(hero2)).value)
